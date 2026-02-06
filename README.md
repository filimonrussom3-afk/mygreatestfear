#  Filimon's Github Project

Filimon Russsom                                                                                                               
Mr. Lam
ICS 3U1
06 February 2026


def page():
    return """<!DOCTYPE html>
<html>
<head>
  <title>Traffic Light Control</title>
  <style>
    body{font-family:Arial;background:#f0f0f0;text-align:center}
    h1{margin-top:20px}
    .panel{display:flex;justify-content:center;gap:40px;margin-top:40px;flex-wrap:wrap}
    .box{background:white;padding:20px;border-radius:12px;box-shadow:0 0 10px #aaa;width:240px}
    .title{font-weight:bold;margin-bottom:20px}
    .row{display:flex;justify-content:space-between;margin-bottom:15px;font-size:16px;align-items:center}
    .switch{position:relative;width:50px;height:24px}
    .switch input{opacity:0}
    .slider{position:absolute;background:#ccc;top:0;left:0;right:0;bottom:0;border-radius:24px}
    .slider:before{content:"";position:absolute;height:18px;width:18px;left:3px;bottom:3px;background:white;border-radius:50%;transition:.3s}
    input:checked+.slider{background:#4CAF50}
    input:checked+.slider:before{transform:translateX(26px)}
  </style>
</head>

<body>
<h1>Traffic Light Control Panel</h1>

<div class="panel">

<div class="box">
  <div class="title">Traffic Mode</div>
  <div class="row">Normal Mode
    <label class="switch"><input type="checkbox" onchange="send('normal',this)"><span class="slider"></span></label>
  </div>
  <div class="row">All Red
    <label class="switch"><input type="checkbox" onchange="send('all_red',this)"><span class="slider"></span></label>
  </div>
  <div class="row">Blink Yellow
    <label class="switch"><input type="checkbox" onchange="send('blink_yellow',this)"><span class="slider"></span></label>
  </div>
</div>

<div class="box">
  <div class="title">Emergency</div>
  <div class="row">NS Green
    <label class="switch"><input type="checkbox" onchange="send('ns_emergency',this)"><span class="slider"></span></label>
  </div>
  <div class="row">EW Green
    <label class="switch"><input type="checkbox" onchange="send('ew_emergency',this)"><span class="slider"></span></label>
  </div>
</div>

<div class="box">
  <div class="title">Railway Crossing</div>
  <div class="row">Train Mode 🚆
    <label class="switch"><input type="checkbox" onchange="send('train_mode',this)"><span class="slider"></span></label>
  </div>
</div>

</div>

<script>
function send(cmd, el){
  if(el.checked){
    document.querySelectorAll('input[type=checkbox]').forEach(cb=>{if(cb!==el) cb.checked=false});
  }
  fetch(`/mode?cmd=${cmd}&state=${el.checked?'on':'off'}`);
}
</script>

</body>
</html>"""

