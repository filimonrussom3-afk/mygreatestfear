import math
import random

class ThreePointerSimulation:
    """Simulates a 3-pointer basketball shot with physics and player stats."""
    
    # Constants
    GRAVITY = 9.81  # m/s^2
    HOOP_HEIGHT = 3.05  # meters (10 feet)
    THREE_POINT_DISTANCE = 7.24  # meters (23 feet 9 inches in NBA)
    
    def __init__(self, player_name, base_accuracy=0.35):
        """
        Initialize a player with shooting stats.
        
        Args:
            player_name: Name of the player
            base_accuracy: Base shooting percentage (0-1)
        """
        self.player_name = player_name
        self.base_accuracy = base_accuracy
        self.shots_taken = 0
        self.shots_made = 0
        
    def calculate_trajectory(self, initial_velocity, launch_angle, release_height=2.2):
        """
        Calculate if the shot makes it based on physics.
        
        Args:
            initial_velocity: Speed of the ball (m/s)
            launch_angle: Angle in degrees
            release_height: Height from which ball is released (meters)
            
        Returns:
            tuple: (makes_shot: bool, trajectory_data: dict)
        """
        angle_rad = math.radians(launch_angle)
        vx = initial_velocity * math.cos(angle_rad)
        vy = initial_velocity * math.sin(angle_rad)
        
        # Time to reach the hoop (horizontal distance)
        if vx == 0:
            return False, {"error": "Horizontal velocity is zero"}
        
        time_to_hoop = self.THREE_POINT_DISTANCE / vx
        
        # Height at the hoop distance
        y_at_hoop = (release_height + 
                     vy * time_to_hoop - 
                     0.5 * self.GRAVITY * time_to_hoop ** 2)
        
        # Check if ball reaches hoop height (within tolerance)
        height_tolerance = 0.15  # 15 cm tolerance
        makes_shot = abs(y_at_hoop - self.HOOP_HEIGHT) <= height_tolerance
        
        trajectory_data = {
            "time_to_hoop": time_to_hoop,
            "height_at_hoop": y_at_hoop,
            "hoop_height": self.HOOP_HEIGHT,
            "distance_from_hoop": abs(y_at_hoop - self.HOOP_HEIGHT)
        }
        
        return makes_shot, trajectory_data
    
    def take_shot(self, pressure_level=0.5):
        """
        Simulate a shot with player tendency and pressure effects.
        
        Args:
            pressure_level: 0-1 scale (0 = no pressure, 1 = maximum pressure)
            
        Returns:
            dict: Shot result details
        """
        self.shots_taken += 1
        
        # Base shot parameters
        ideal_velocity = 7.5  # m/s
        ideal_angle = 52  # degrees
        
        # Add variance based on pressure and skill
        velocity_variance = random.gauss(0, 0.3 * (1 + pressure_level))
        angle_variance = random.gauss(0, 2 * (1 + pressure_level))
        
        velocity = ideal_velocity + velocity_variance
        angle = ideal_angle + angle_variance
        
        # Adjust accuracy based on pressure
        pressure_penalty = pressure_level * 0.15
        adjusted_accuracy = max(0, self.base_accuracy - pressure_penalty)
        
        # Random determination with adjusted accuracy
        if random.random() < adjusted_accuracy:
            makes_shot = True
            self.shots_made += 1
        else:
            # Still calculate trajectory for missed shots
            makes_shot, _ = self.calculate_trajectory(velocity, angle)
            if makes_shot:
                self.shots_made += 1
        
        result = {
            "player": self.player_name,
            "shot_number": self.shots_taken,
            "made": makes_shot,
            "velocity": round(velocity, 2),
            "angle": round(angle, 2),
            "pressure": pressure_level,
            "three_pointers": self.shots_made,
            "attempts": self.shots_taken,
            "percentage": round((self.shots_made / self.shots_taken) * 100, 1)
        }
        
        return result
    
    def take_multiple_shots(self, num_shots=10, pressure_level=0.5):
        """
        Simulate multiple shots.
        
        Args:
            num_shots: Number of shots to take
            pressure_level: 0-1 scale
            
        Returns:
            list: Results of all shots
        """
        results = []
        for _ in range(num_shots):
            result = self.take_shot(pressure_level)
            results.append(result)
        
        return results


# Example usage
if __name__ == "__main__":
    print("🏀 3-Pointer Basketball Shot Simulator\n")
    
    # Create player
    player = ThreePointerSimulation("LeBron James", base_accuracy=0.40)
    
    print(f"Player: {player.player_name}")
    print(f"Base 3P%: {player.base_accuracy * 100}%\n")
    
    # Simulate game situation
    print("=" * 60)
    print("REGULAR SITUATION (Low Pressure)")
    print("=" * 60)
    results_low = player.take_multiple_shots(num_shots=5, pressure_level=0.2)
    
    for result in results_low:
        status = "✓ MADE!" if result["made"] else "✗ MISSED"
        print(f"Shot {result['shot_number']}: {status}")
        print(f"  Velocity: {result['velocity']} m/s | Angle: {result['angle']}°")
        print(f"  Season Record: {result['three_pointers']}/{result['attempts']} ({result['percentage']}%)\n")
    
    # Reset for high pressure scenario
    player2 = ThreePointerSimulation("LeBron James", base_accuracy=0.40)
    
    print("=" * 60)
    print("CLUTCH SITUATION (High Pressure - Finals)")
    print("=" * 60)
    results_high = player2.take_multiple_shots(num_shots=5, pressure_level=0.8)
    
    for result in results_high:
        status = "✓ MADE!" if result["made"] else "✗ MISSED"
        print(f"Shot {result['shot_number']}: {status}")
        print(f"  Velocity: {result['velocity']} m/s | Angle: {result['angle']}°")
        print(f"  Season Record: {result['three_pointers']}/{result['attempts']} ({result['percentage']}%)\n")
