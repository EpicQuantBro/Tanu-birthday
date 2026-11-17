import html
import random

import streamlit as st
import streamlit.components.v1 as components

# ─────────────────────────────────────────────────────────────
#  ✍️  WRITE YOUR LETTER HERE  (between the triple quotes)
#  Line breaks and blank lines are kept exactly as you type them.
# ─────────────────────────────────────────────────────────────
LETTER = """My dearest Tanu,

Happy Birthday, my love.

Write everything you want to say to her here.
Tell her why she matters, your favourite memories,
the little things you love about her, and what you
hope for her this year.

Forever yours,
[Your name] ❤️
"""

st.set_page_config(
    page_title="Happy Birthday Tanu ❤️",
    page_icon="❤️",
    layout="centered",
)

if "page" not in st.session_state:
    st.session_state.page = "home"

# ─────────────────────────────────────────────────────────────
#  Shared styling (hides Streamlit chrome, pink background)
# ─────────────────────────────────────────────────────────────
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Pacifico&family=Quicksand:wght@500;700&display=swap');

    #MainMenu, header, footer {visibility: hidden;}
    .stApp {
        background: linear-gradient(180deg, #ffe3ec 0%, #ffc2d4 55%, #ff9fb8 100%);
        overflow-x: hidden;
    }
    .block-container {padding-top: 2rem;}

    div.stButton {display: flex; justify-content: center;}
    div.stButton > button {
        font-family: 'Quicksand', sans-serif;
        font-weight: 700;
        font-size: 1.2rem;
        color: #fff;
        background: #e0245e;
        border: none;
        border-radius: 999px;
        padding: 0.8rem 2rem;
        box-shadow: 0 8px 20px rgba(224, 36, 94, 0.45);
        transition: transform 0.15s ease, box-shadow 0.15s ease;
    }
    div.stButton > button:hover {
        color: #fff;
        background: #c81a50;
        transform: translateY(-2px) scale(1.04);
        box-shadow: 0 12px 26px rgba(224, 36, 94, 0.55);
    }
    div.stButton > button:focus:not(:active) {color: #fff; border: none;}
    </style>
    """,
    unsafe_allow_html=True,
)


# ─────────────────────────────────────────────────────────────
#  PAGE 1 – Birthday greeting + floating balloons
# ─────────────────────────────────────────────────────────────
def home_page():
    colors = ["#ff4d6d", "#ff85a1", "#ffb3c6", "#c9184a", "#ffd166", "#b794f4", "#74c0fc"]
    balloons = ""
    for _ in range(22):
        left = random.randint(0, 96)
        size = random.randint(46, 84)
        duration = random.uniform(9, 17)
        delay = random.uniform(-17, 0)  # negative = already mid-flight on load
        sway = random.randint(-40, 40)
        color = random.choice(colors)
        balloons += (
            f'<div class="balloon" style="left:{left}vw;width:{size}px;height:{size * 1.2:.0f}px;'
            f"background:radial-gradient(circle at 32% 28%, #ffffffaa 0, {color} 38%, {color} 100%);"
            f"animation-duration:{duration:.1f}s;animation-delay:{delay:.1f}s;--sway:{sway}px;"
            f'"></div>'
        )

    st.markdown(
        f"""
        <style>
        .balloon-layer {{
            position: fixed; inset: 0; pointer-events: none; z-index: 0; overflow: hidden;
        }}
        .balloon {{
            position: absolute; bottom: -140px;
            border-radius: 50% 50% 48% 48% / 55% 55% 45% 45%;
            box-shadow: inset -8px -10px 18px rgba(0,0,0,0.12);
            animation-name: floatUp; animation-timing-function: ease-in-out;
            animation-iteration-count: infinite;
        }}
        .balloon::after {{
            content: ""; position: absolute; left: 50%; top: 100%;
            width: 1.5px; height: 70px; background: rgba(90,50,60,0.45);
        }}
        @keyframes floatUp {{
            0%   {{ transform: translate(0, 0) rotate(-4deg); opacity: 0.95; }}
            50%  {{ transform: translate(var(--sway), -60vh) rotate(5deg); }}
            100% {{ transform: translate(calc(var(--sway) * -1), -125vh) rotate(-4deg); opacity: 0.95; }}
        }}
        .hb-title {{
            position: relative; z-index: 2; text-align: center;
            font-family: 'Pacifico', cursive;
            font-size: clamp(2.6rem, 9vw, 5.2rem);
            line-height: 1.2; color: #b0124a;
            margin: 22vh 0 2.5rem 0;
            text-shadow: 0 4px 0 #fff, 0 10px 24px rgba(176, 18, 74, 0.35);
        }}
        div.stButton {{ position: relative; z-index: 2; }}
        @media (prefers-reduced-motion: reduce) {{ .balloon {{ animation: none; bottom: 20vh; }} }}
        </style>
        <div class="balloon-layer">{balloons}</div>
        <div class="hb-title">Happy Birthday Tanu ❤️</div>
        """,
        unsafe_allow_html=True,
    )

    if st.button("click here for a smol lil gift 🎁"):
        st.session_state.page = "gift"
        st.rerun()


# ─────────────────────────────────────────────────────────────
#  PAGE 2 – Big letter + clickable hearts that explode into "I love you"
# ─────────────────────────────────────────────────────────────
GIFT_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link href="https://fonts.googleapis.com/css2?family=Dancing+Script:wght@600;700&family=Pacifico&display=swap" rel="stylesheet">
<style>
  * { box-sizing: border-box; }
  html, body { margin: 0; background: transparent; font-family: 'Dancing Script', cursive; }
  #stage { position: relative; width: 100%; min-height: 1500px; padding: 30px 12px 60px; overflow: hidden; }

  .letter {
    position: relative; z-index: 1; max-width: 760px; margin: 0 auto;
    background: #fffaf3; border-radius: 6px; padding: 56px 48px 64px;
    box-shadow: 0 20px 50px rgba(120, 20, 50, 0.28);
    background-image: repeating-linear-gradient(transparent 0, transparent 53px, #f3d9df 54px);
    background-position: 0 56px;
  }
  .letter h1 { font-family: 'Pacifico', cursive; color: #b0124a; font-size: 2.2rem; margin: 0 0 26px; font-weight: 400; }
  .letter .body {
    white-space: pre-wrap; color: #4a1f2e; font-size: 2.1rem; line-height: 54px; font-weight: 600;
  }

  #hearts { position: absolute; inset: 0; z-index: 5; pointer-events: none; perspective: 700px; }

  .heart {
    position: absolute; pointer-events: auto; cursor: pointer;
    transform-style: preserve-3d;
    animation: pop 0.5s cubic-bezier(.2,1.6,.4,1) both, spin 5s ease-in-out infinite 0.5s;
    filter: drop-shadow(0 10px 8px rgba(120, 0, 30, 0.45));
    transition: filter 0.2s;
  }
  .heart:hover { filter: drop-shadow(0 14px 12px rgba(120, 0, 30, 0.6)) brightness(1.12); }
  .heart svg { display: block; width: 100%; height: 100%; }

  @keyframes pop  { from { transform: scale(0) rotateY(0); } to { transform: scale(1) rotateY(0); } }
  @keyframes spin { 0%,100% { transform: rotateY(-28deg) rotateX(6deg); } 50% { transform: rotateY(28deg) rotateX(-6deg); } }

  .ily {
    position: absolute; z-index: 6; pointer-events: none; white-space: nowrap;
    font-family: 'Pacifico', cursive; color: #e0245e; font-size: 2.1rem;
    transform: translate(-50%, -50%);
    text-shadow: 0 0 12px #fff, 0 0 4px #fff, 0 4px 14px rgba(224,36,94,.55);
    animation: ily 1.7s ease-out forwards;
  }
  @keyframes ily {
    0%   { opacity: 0; transform: translate(-50%, -50%) scale(.2); }
    20%  { opacity: 1; transform: translate(-50%, -60%) scale(1.25); }
    70%  { opacity: 1; transform: translate(-50%, -90%) scale(1); }
    100% { opacity: 0; transform: translate(-50%, -140%) scale(1); }
  }

  .bit {
    position: absolute; z-index: 6; pointer-events: none; color: #e0245e;
    animation: burst 1s ease-out forwards;
  }
  @keyframes burst {
    0%   { opacity: 1; transform: translate(-50%, -50%) scale(.4); }
    100% { opacity: 0; transform: translate(calc(-50% + var(--dx)), calc(-50% + var(--dy))) scale(1.1) rotate(var(--rot)); }
  }

  @media (max-width: 600px) {
    .letter { padding: 36px 22px 44px; }
    .letter .body { font-size: 1.65rem; line-height: 46px; }
    .letter { background-image: repeating-linear-gradient(transparent 0, transparent 45px, #f3d9df 46px); background-position: 0 50px; }
  }
  @media (prefers-reduced-motion: reduce) { .heart { animation: pop .3s both; } }
</style>
</head>
<body>
<div id="stage">
  <div class="letter">
    <h1>For Tanu ❤️</h1>
    <div class="body">__LETTER__</div>
  </div>
  <div id="hearts"></div>
</div>

<script>
  const layer = document.getElementById('hearts');
  const stage = document.getElementById('stage');
  const HEART_COUNT = 6;
  const MESSAGES = ["I love you", "I love you ❤️", "I love you", "love you so much", "I love you"];

  const heartSVG = `
    <svg viewBox="0 0 100 90" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <radialGradient id="g" cx="32%" cy="26%" r="80%">
          <stop offset="0%"  stop-color="#ff9aa8"/>
          <stop offset="35%" stop-color="#f0204f"/>
          <stop offset="100%" stop-color="#8f0a2c"/>
        </radialGradient>
      </defs>
      <path d="M50 86 C10 56 2 34 2 24 C2 11 12 2 25 2 C36 2 45 8 50 17 C55 8 64 2 75 2 C88 2 98 11 98 24 C98 34 90 56 50 86 Z" fill="url(#g)"/>
      <ellipse cx="30" cy="22" rx="11" ry="6" fill="#fff" opacity=".55" transform="rotate(-30 30 22)"/>
    </svg>`;

  const rand = (a, b) => a + Math.random() * (b - a);

  function spawnHeart() {
    const size = rand(60, 92);
    const w = layer.clientWidth, h = layer.clientHeight;
    const el = document.createElement('div');
    el.className = 'heart';
    el.style.width = size + 'px';
    el.style.height = size * 0.9 + 'px';
    el.style.left = rand(8, Math.max(20, w - size - 8)) + 'px';
    el.style.top  = rand(20, Math.max(40, h - size - 20)) + 'px';
    el.innerHTML = heartSVG.replace(/id="g"/, 'id="g' + Math.random().toString(36).slice(2) + '"');
    // give each heart its own gradient id so they never clash
    const gid = el.querySelector('radialGradient').id;
    el.querySelector('path').setAttribute('fill', 'url(#' + gid + ')');
    el.addEventListener('click', () => explode(el));
    layer.appendChild(el);
  }

  function explode(el) {
    const r = el.getBoundingClientRect();
    const lr = layer.getBoundingClientRect();
    const cx = r.left - lr.left + r.width / 2;
    const cy = r.top - lr.top + r.height / 2;
    el.remove();

    // "I love you" text
    const t = document.createElement('div');
    t.className = 'ily';
    t.textContent = MESSAGES[Math.floor(Math.random() * MESSAGES.length)];
    t.style.left = cx + 'px';
    t.style.top = cy + 'px';
    layer.appendChild(t);
    setTimeout(() => t.remove(), 1700);

    // little hearts flying out
    for (let i = 0; i < 16; i++) {
      const b = document.createElement('div');
      b.className = 'bit';
      b.textContent = '❤';
      const angle = (Math.PI * 2 * i) / 16 + rand(-0.2, 0.2);
      const dist = rand(60, 150);
      b.style.left = cx + 'px';
      b.style.top = cy + 'px';
      b.style.fontSize = rand(14, 28) + 'px';
      b.style.setProperty('--dx', Math.cos(angle) * dist + 'px');
      b.style.setProperty('--dy', Math.sin(angle) * dist + 'px');
      b.style.setProperty('--rot', rand(-120, 120) + 'deg');
      layer.appendChild(b);
      setTimeout(() => b.remove(), 1000);
    }

    // a new heart appears somewhere else
    setTimeout(spawnHeart, 900);
  }

  for (let i = 0; i < HEART_COUNT; i++) setTimeout(spawnHeart, i * 150);
</script>
</body>
</html>
"""


def gift_page():
    letter_html = html.escape(LETTER.strip("\n"))
    page = GIFT_TEMPLATE.replace("__LETTER__", letter_html)
    components.html(page, height=1500, scrolling=True)

    if st.button("⬅ back"):
        st.session_state.page = "home"
        st.rerun()


# ─────────────────────────────────────────────────────────────
#  Router
# ─────────────────────────────────────────────────────────────
if st.session_state.page == "home":
    home_page()
else:
    gift_page()
