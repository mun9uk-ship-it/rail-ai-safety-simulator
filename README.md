<h1 align="center">🚆 Rail AI Safety Simulator</h1>
<h3 align="center">Enhancing Digital Signaling Safety: AI-Based Derailment & Collision Avoidance</h3>
<h3 align="center" dir="rtl">تحسين أمان الإشارات الرقمية: محاكي استباق الانحراف ومنع التصادم بالذكاء الاصطناعي</h3>

<p align="center">
  <img src="https://img.shields.io/badge/-Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54">
  <img src="https://img.shields.io/badge/Framework-Streamlit-FF4B4B.svg?style=for-the-badge">
  <img src="https://img.shields.io/badge/ML%20Library-Scikit--Learn-F79E1E.svg?style=for-the-badge">
</p>

<hr>

<h2>📸 Live Demo</h2>

<p align="center">
  <img src="rail-ai-safety-simulator.png" alt="Rail AI Safety Simulator dashboard showing live telemetry, signal status, and emergency braking analysis" width="850">
</p>

<p align="center">
  🔗 <a href="https://mun9uk-ship-it-rail-ai-safety-simulator-v01-yj0ycc.streamlit.app/"><b>Launch the live simulator in your browser</b></a>
</p>

<hr>

<h2>📖 Project Overview</h2>

<p>
This project is an AI-powered simulation built to explore digital railway
signaling and safety. It analyses simulated real-time sensor telemetry
(track vibration) using an <b>Isolation Forest anomaly detection model</b>
to flag potential derailment events or track faults.
</p>

<p>
When a critical anomaly is flagged, the app calculates emergency braking
physics — reaction time, required stopping distance, and deceleration —
and automatically triggers a fail-safe braking action to stop the trailing
train and prevent a collision.
</p>

<h2 dir="rtl">📖 نبذة عن المشروع</h2>

<p dir="rtl">
هذا المشروع عبارة عن محاكاة مدعومة بالذكاء الاصطناعي لاستكشاف أمان
الإشارات الرقمية في السكك الحديدية. يحلل بيانات اهتزاز افتراضية للمسار
باستخدام <b>نموذج Isolation Forest لكشف الشذوذ</b> للتنبؤ بحالات
انحراف محتملة أو أعطال في المسار.
</p>

<p dir="rtl">
عند رصد خطر حرج، يحسب النظام فوراً معادلات الكبح الطارئ — زمن
الاستجابة، مسافة التوقف اللازمة، ومعدل التباطؤ — ويفعّل تلقائياً
إجراء فرملة آمن لإيقاف القطار الخلفي ومنع التصادم.
</p>

<hr>

<h2>⚙️ Core Features</h2>

<ul>
  <li><b>AI Anomaly Detection:</b> Isolation Forest model trained to spot abnormal track vibration readings</li>
  <li><b>Physics-Based Braking Calculations:</b> Real-time deceleration, braking distance, and total stopping time</li>
  <li><b>Bilingual Dashboard:</b> Full English and Arabic labels throughout the UI</li>
  <li><b>Live Interactive Telemetry:</b> Real-time line charts of vibration and train speed</li>
</ul>

<hr>

<h2>🛠️ Installation & Requirements</h2>

<p>Requires <b>Python 3.9+</b>.</p>

<pre><code>git clone https://github.com/mun9uk-ship-it/rail-ai-safety-simulator.git
cd rail-ai-safety-simulator
pip install streamlit pandas numpy scikit-learn
</code></pre>

<h2>🚀 How to Run</h2>

<pre><code>streamlit run v01.py
</code></pre>

<p>This opens the simulator locally at <code>http://localhost:8501</code>.</p>

<p>Or skip setup entirely and try the
<a href="https://mun9uk-ship-it-rail-ai-safety-simulator-v01-yj0ycc.streamlit.app/">hosted version</a>.</p>

<h2>💡 How to Use</h2>

<ol>
  <li>Click <b>▶️ Run Normal Simulation</b> to watch both trains operate safely under standard conditions</li>
  <li>Click <b>⚠️ Simulate Track Fault (Watford)</b> to introduce a high-vibration anomaly and watch the AI detect it and trigger automatic emergency braking</li>
  <li>Click <b>🔄 Reset System</b> to clear the run and return to default positions</li>
</ol>

<hr>

<h2>🧠 How I built this</h2>

<p>
I have hands-on experience with rail ticketing, revenue protection, and
an OPC train-driver aptitude certification, and I'm currently applying my
AI/ML coursework (IBM AI Fundamentals, Machine Learning with Python) to
transport-safety style problems. I used an AI coding assistant to help
write and structure this app, and worked through the logic — the
Isolation Forest model, the object-oriented <code>Train</code> class, and the
braking-physics calculations — to make sure I understand exactly how and
why it works.
</p>

<h2 dir="rtl">🧠 كيف بنيت هذا المشروع</h2>

<p dir="rtl">
لدي خبرة عملية في تذاكر السكك الحديدية وحماية الإيرادات، وشهادة اجتياز
اختبار OPC لسائق قطار، وأطبّق حالياً ما تعلمته في دورات الذكاء
الاصطناعي (IBM AI Fundamentals، تعلم الآلة ببايثون) على مسائل تشبه
أمان النقل. استخدمت مساعد ذكاء اصطناعي في كتابة وهيكلة هذا التطبيق،
وراجعت المنطق بالكامل — نموذج Isolation Forest، وكلاس <code>Train</code>،
وحسابات فيزياء الكبح — للتأكد أنني أفهم تماماً كيف ولماذا يعمل.
</p>

<hr>

<h2>⚠️ Limitations</h2>

<ul>
  <li>All telemetry (track vibration) is <b>simulated</b>, not real sensor data</li>
  <li>This is a learning/portfolio project, not a certified or validated safety system</li>
  <li>A real deployment would require real sensor integration, domain-expert validation, and formal safety-case testing</li>
</ul>
