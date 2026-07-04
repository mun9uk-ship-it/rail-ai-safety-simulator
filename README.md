<!-- Tab Navigation Headers -->
<div align="center">
  <h1>🚆 Enhancing Digital Signaling Safety / تحسين أمان الإشارات الرقمية</h1>
  <p>Select your preferred language below / اختر اللغة المفضلة أدناه:</p>
  <a href="#english-version"><b>🇬🇧 English Documentation</b></a> | 
  <a href="#arabic-version"><b>🇸🇦 الوثائق باللغة العربية</b></a>
</div>

<hr />

<!-- ========================================== -->
<!--             ENGLISH VERSION                -->
<!-- ========================================== -->
<div id="english-version">
  <h2 align="center">🇬🇧 Project Documentation (English)</h2>
  
  <p align="center">
    <img src="https://img.shields.io/badge/Python-3.9+-blue.svg" alt="Python Version">
    <img src="https://img.shields.io/badge/Framework-Streamlit-FF4B4B.svg" alt="Streamlit">
    <img src="https://img.shields.io/badge/ML%20Library-Scikit--Learn-F7931E.svg" alt="Scikit-Learn">
  </p>

  <h3>📖 Project Overview</h3>
  <p>
    This repository contains an AI-powered simulation framework built to address digital railway signaling and safety. By analyzing real-time virtual sensor telemetry (such as structural track vibrations), the system uses an <b>Isolation Forest anomaly detection model</b> to predict potential derailment events or track faults immediately. 
  </p>
  <p>
    When a critical risk is flagged, the application instantly calculates emergency braking physics—accounting for reaction delay, required stopping distance, and deceleration rates—to automatically trigger a fail-safe interlocking action that stops trailing trains and prevents catastrophic collisions.
  </p>

  <h3>⚙️ Core Features</h3>
  <ul>
    <li><b>AI Anomaly Detection:</b> Machine learning engine trained to spot abnormal track vibration signatures (G-force anomalies).</li>
    <li><b>Physics-Based Fail-Safe Calculations:</b> Real-time processing of deceleration, braking window, and total stopping time.</li>
    <li><b>Bilingual UI Dashboard:</b> Full native English and Arabic descriptions and metric readouts.</li>
    <li><b>Live Interactive Telemetry:</b> Dynamic real-time graphing, block signaling updates, and status tracking.</li>
  </ul>

  <h3>🛠️ Installation & Requirements</h3>
  <p>To run this simulation locally, you will need <b>Python 3.9 or higher</b> installed on your system.</p>

  <h4>1. Clone the Repository</h4>
  <pre><code>git clone https://github.com/YOUR_USERNAME/rail-ai-safety-simulator.git
cd rail-ai-safety-simulator</code></pre>

  <h4>2. Install Required Libraries</h4>
  <p>Install the necessary dependencies using pip:</p>
  <pre><code>pip install streamlit pandas numpy scikit-learn</code></pre>

  <blockquote>
    <b>Note:</b> If you plan on deploying directly to Streamlit Community Cloud, make sure to include a <code>requirements.txt</code> file in your root folder containing:
    <br />
    <code>streamlit</code><br />
    <code>pandas</code><br />
    <code>numpy</code><br />
    <code>scikit-learn</code>
  </blockquote>

  <h3>🚀 How to Run</h3>
  <p>Launch the application using Streamlit from your terminal by targeting your entry point script:</p>
  <pre><code>streamlit run v01.py</code></pre>
  <p>Once the local server initializes, a browser tab will automatically open at <code>http://localhost:8501</code>.</p>

  <h3>OR</h3>
  <a href="https://mun9uk-ship-it-rail-ai-safety-simulator-v01-yj0ycc.streamlit.app/"><b> click to run it DIRECT in your browser </b></a>


  <h3>💡 How to Use the Simulation</h3>
  <ol>
    <li>Click <b>▶️ Run Normal Simulation</b> to see the trains operate safely under standard baseline parameters.</li>
    <li>Click <b>⚠️ Simulate Track Fault (Watford)</b> to introduce high G-force anomalies on the track layout. Watch how the AI flags the danger and triggers automated defensive braking.</li>
    <li>Click <b>🔄 Reset System</b> to clear current execution history and return to default positions.</li>
  </ol>
</div>

<hr />

<!-- ========================================== -->
<!--             ARABIC VERSION                 -->
<!-- ========================================== -->
<div id="arabic-version" dir="rtl">
  <h2 align="center">🇸🇦 توثيق المشروع (باللغة العربية)</h2>
  
  <p align="center">
    <img src="https://img.shields.io/badge/لغة_البرمجة-Python_3.9+-blue.svg" alt="نسخة بايثون">
    <img src="https://img.shields.io/badge/إطار_العمل-Streamlit-FF4B4B.svg" alt="ستريمليت">
    <img src="https://img.shields.io/badge/مكتبة_الذكاء_الاصطناعي-Scikit--Learn-F7931E.svg" alt="سايكيت ليرن">
  </p>

  <h3>📖 نبذة عن المشروع</h3>
  <p>
    يحتوي هذا المستودع على بيئة محاكاة برمجية مدعومة بالذكاء الاصطناعي تم تطويرها لتعزيز أمان الإشارات الرقمية في السكك الحديدية من خلال تحليل قياسات مستشعرات الاهتزاز الفورية للهيكل السفلي للمسار، يعتمد النظام على <b>نموذج Isolation Forest لرصد البيانات الشاذة</b>  للتنبؤ بحالات انحراف القطارات أو عيوب السكك الحديدية بشكل فوري.
  </p>
  <p>
    عند اكتشاف خطر حرج، يقوم التطبيق فوراً بحساب المعادلات الفيزيائية لكبح الطوارئ — مع الأخذ في الاعتبار زمن استجابة النظام الفني، ومسافة الكبح المطلوبة، ومعدلات التباطؤ  — لتفعيل نظام الارتباط الآمن آلياً وتأمين القطارات الخلفية لمنع وقوع حوادث التصادم .
  </p>

  <h3>⚙️ الميزات الأساسية</h3>
  <ul>
    <li><b>رصد الخلل بالذكاء الاصطناعي:</b> محرك تعلم آلي مدرب على رصد أنماط الاهتزاز غير الطبيعية (قوى الجاذبية الشاذة G-force) في السكة .</li>
    <li><b>حسابات الأمان الفيزيائية:</b> معالجة فورية لحسابات التباطؤ، مسافة الكبح، وإجمالي زمن التوقف التام .</li>
    <li><b>واجهة مستخدم ثنائية اللغة:</b> دعم كامل باللغتين العربية والإنجليزية لجميع القراءات والمؤشرات .</li>
    <li><b>تحليلات بيانية حية:</b> رسوم بيانية ديناميكية مباشرة، وتحديثات مستمرة لحالة الإشارات والTelemetry .</li>
  </ul>

  <h3>🛠️ التثبيت والمتطلبات</h3>
  <p>لتشغيل هذه المحاكاة محلياً على جهازك، ستحتاج إلى إصدار <b>Python 3.9 أو أعلى</b>.</p>

  <h4>1. استنساخ المستودع (Clone)</h4>
  <pre><code>git clone https://github.com/YOUR_USERNAME/rail-ai-safety-simulator.git
cd rail-ai-safety-simulator</code></pre>

  <h4>2. تثبيت المكتبات المطلوبة</h4>
  <p>قم بتثبيت الحزم اللازمة باستخدام pip:</p>
  <pre><code>pip install streamlit pandas numpy scikit-learn</code></pre>

  <blockquote>
    <b>ملاحظة:</b> إذا كنت تخطط لرفع المشروع مباشرة على سحابة Streamlit Cloud، تأكد من تضمين ملف <code>requirements.txt</code> في المجلد الرئيسي يحتوي على المكتبات التالية:
    <br />
    <code>streamlit</code><br />
    <code>pandas</code><br />
    <code>numpy</code><br />
    <code>scikit-learn</code>
  </blockquote>

  <h3>🚀 كيفية التشغيل</h3>
  <p>قم بتشغيل التطبيق عبر الطرفية (Terminal) بتوجيه الأمر نحو ملف التشغيل:</p>
  <pre><code>streamlit run v01.py</code></pre>
  <p>بعد بدء الخادم المحلي، سيفتح المتصفح تلقائياً صفحة المحاكاة على الرابط <code>http://localhost:8501</code>.</p>

  <h3>💡 دليل استخدام المحاكاة</h3>
  <ol>
    <li>اضغط على <b>▶️ Run Normal Simulation / تشغيل محاكاة طبيعية</b> لمتابعة حركة القطارات الآمنة تحت الظروف العادية .</li>
    <li>اضغط على <b>⚠️ Simulate Track Fault (Watford) / محاكاة خلل السكة (واتفورد)</b> لتوليد اهتزازات شاذة وخطيرة على المسار ، وراقب كيف يكتشف الذكاء الاصطناعي الخطر ويفعّل كبح الطوارئ التلقائي .</li>
    <li>اضغط على <b>🔄 Reset System / إعادة ضبط النظام</b> لمسح سجل المحاكاة الحالي وإعادة القطارات إلى وضعها الافتراضي .</li>
  </ol>
</div>
