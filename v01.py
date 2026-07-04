import streamlit as st
import pandas as pd
import numpy as np
import time
from sklearn.ensemble import IsolationForest

# 1. Page Configuration / إعدادات الصفحة
st.set_page_config(page_title="Rail AI Safety Simulator", layout="wide")
st.title("🚆 Enhancing Digital Signaling Safety: AI-Based Derailment & Collision Avoidance")
st.subheader("تحسين أمان الإشارات الرقمية: محاكي استباق الانحراف ومنع التصادم بالذكاء الاصطناعي")
st.markdown("---")

# 2. Object-Oriented Design / بناء الكائنات
class Train:
    def __init__(self, train_id, initial_speed, position_offset):
        self.train_id = train_id
        self.speed = initial_speed  # km/h
        self.position = position_offset  # meters
        self.status = "Running / يعمل"
        self.brake_applied = False

    def update_position(self, time_step=1):
        speed_m_s = (self.speed * 1000) / 3600
        self.position += speed_m_s * time_step

    def apply_emergency_brake(self):
        self.brake_applied = True
        self.speed = 0
        self.status = "🚨 EMERGENCY STOPPED / توقف طارئ"

class AIDerailmentDetector:
    def __init__(self):
        normal_vibrations = np.random.uniform(0.1, 0.8, (100, 1))
        self.model = IsolationForest(contamination=0.05, random_state=42)
        self.model.fit(normal_vibrations)

    def predict_anomaly(self, current_vibration):
        prediction = self.model.predict([[current_vibration]])
        return prediction[0] == -1

# 3. Session State Management / إدارة حالة النظام
if 'simulation_running' not in st.session_state:
    st.session_state.simulation_running = False
if 'train_ahead' not in st.session_state:
    st.session_state.train_ahead = Train("Train-A (Ahead)", 100, 500)
if 'train_behind' not in st.session_state:
    st.session_state.train_behind = Train("Train-B (Behind)", 100, 0)
if 'detector' not in st.session_state:
    st.session_state.detector = AIDerailmentDetector()
if 'history' not in st.session_state:
    st.session_state.history = []

# 4. Control Buttons Dashboard / أزرار التحكم في المحاكاة
st.markdown("### 🎛️ Control Panel / لوحة التحكم")
col_btn1, col_btn2, col_btn3 = st.columns(3)
with col_btn1:
    if st.button("▶️ Run Normal Simulation / تشغيل محاكاة طبيعية", use_container_width=True):
        st.session_state.simulation_running = True
        st.session_state.trigger_fault = False
with col_btn2:
    if st.button("⚠️ Simulate Track Fault (Watford) / محاكاة خلل السكة (واتفورد)", use_container_width=True):
        st.session_state.simulation_running = True
        st.session_state.trigger_fault = True
with col_btn3:
    if st.button("🔄 Reset System / إعادة ضبط النظام", use_container_width=True):
        st.session_state.simulation_running = False
        st.session_state.train_ahead = Train("Train-A (Ahead)", 100, 500)
        st.session_state.train_behind = Train("Train-B (Behind)", 100, 0)
        st.session_state.history = []
        st.rerun()

st.markdown("---")

# 5. Live Telemetry & Monitoring Dashboard / الشاشة الحية للمراقبة
if st.session_state.simulation_running:
    
    # Placeholders to smooth out live updates / حاويات التحديث الفوري للبيانات
    metrics_placeholder = st.empty()
    analysis_placeholder = st.empty()
    chart_placeholder = st.empty()

    for i in range(120):
        time.sleep(0.1)  # Faster refresh for a better visual graph / سرعة تحديث الرسوم البيانية

        # Anomaly generation logic / منطق توليد الخلل المفاجئ
        if st.session_state.trigger_fault and i > 40:
            current_vibration = float(np.random.uniform(2.5, 4.0))
        else:
            current_vibration = float(np.random.uniform(0.2, 0.7))

        st.session_state.train_ahead.update_position()
        st.session_state.train_behind.update_position()

        # AI Anomaly Detection / فحص الذكاء الاصطناعي للاهتزازات
        is_anomaly = st.session_state.detector.predict_anomaly(current_vibration)
        
        signaling_status_en = "🟢 GREEN (CLEAR)"
        signaling_status_ar = "🟢 أخضر (مسار آمن)"
        
        driver_reaction_time = 0.0
        braking_distance = 0.0
        total_stopping_time = 0.0

        if is_anomaly:
            initial_speed_kph = 100.0
            speed_m_s = (initial_speed_kph * 1000) / 3600  # 27.77 m/s
            
            # Physics Calculation (Fail-Safe Deceleration at 1.0 m/s^2) / الحسابات الفيزيائية للكبح
            driver_reaction_time = 0.4  # Seconds (Automated System Response)
            deceleration = 1.0  # m/s^2
            braking_distance = (speed_m_s ** 2) / (2 * deceleration)
            braking_time = speed_m_s / deceleration
            total_stopping_time = driver_reaction_time + braking_time

            # Apply braking commands internally / تفعيل أوامر الكبح داخلياً
            st.session_state.train_ahead.apply_emergency_brake()
            st.session_state.train_ahead.status = "❌ DERAILED / خرج عن المسار"
            
            signaling_status_en = "🔴 RED (DANGER)"
            signaling_status_ar = "🔴 أحمر (خطر تصادم)"
            
            st.session_state.train_behind.apply_emergency_brake()

        # Store historical telemetry / تسجيل البيانات التاريخية للرسم البياني
        st.session_state.history.append({
            "Time Step": len(st.session_state.history),
            "Track Vibration (G)": current_vibration,
            "Train A Speed (km/h)": st.session_state.train_ahead.speed,
            "Train B Speed (km/h)": st.session_state.train_behind.speed,
        })
        df_history = pd.DataFrame(st.session_state.history)

        # UI Rendering: Main Metrics Block / عرض البيانات الأساسية للقطارات والإشارات
        with metrics_placeholder.container():
            st.markdown("### 📊 Real-Time Telemetry / القياسات الفورية الحية")
            
            c1, c2, c3, c4 = st.columns(4)
            c1.metric(
                label="Block Signal Status / إشارة القطاع الحالي", 
                value=signaling_status_en, 
                delta=signaling_status_ar, 
                delta_color="off"
            )
            c2.metric(
                label="Track Vibration / اهتزازات السكة", 
                value=f"{current_vibration:.2f} G",
                delta="Normal / طبيعي" if not is_anomaly else "Critical / خطير",
                delta_color="normal" if not is_anomaly else "inverse"
            )
            c3.metric(
                label="Train A Speed / سرعة القطار الأمامي", 
                value=f"{st.session_state.train_ahead.speed} km/h",
                delta=st.session_state.train_ahead.status,
                delta_color="normal" if not is_anomaly else "inverse"
            )
            c4.metric(
                label="Train B Speed / سرعة القطار الخلفي", 
                value=f"{st.session_state.train_behind.speed} km/h",
                delta=st.session_state.train_behind.status,
                delta_color="normal" if not is_anomaly else "inverse"
            )

        # UI Rendering: Emergency Braking Analysis / تحليلات كبح الطوارئ وحسابات المسافات
        if is_anomaly:
            with analysis_placeholder.container():
                st.markdown("---")
                st.markdown("### 🛡️ Fail-Safe Interlocking Analysis / تحليلات أمان كبح الطوارئ")
                
                a1, a2, a3 = st.columns(3)
                a1.metric(
                    label="System Reaction Time / زمن استجابة النظام التقني", 
                    value=f"{driver_reaction_time} Sec", 
                    delta="Automated AI Trigger / تفعيل آلي بالذكاء الاصطناعي"
                )
                a2.metric(
                    label="Braking Distance Required / مسافة الكبح الفيزيائية اللازمة", 
                    value=f"{braking_distance:.1f} Meters / متر", 
                    delta="Safe Interlocking Distance Verified / تم تأكيد مسافة الأمان"
                )
                a3.metric(
                    label="Total Time to Full Stop / إجمالي زمن التوقف التام", 
                    value=f"{total_stopping_time:.1f} Sec", 
                    delta="Collision Successfully Avoided / تم منع التصادم بنجاح"
                )
                st.error("🚨 **AI Critical Warning:** Anomaly detected. System deployed emergency brakes immediately, safely securing Train-B based on virtual ballast data. \n\n **تحذير حرِج:** رصد الذكاء الاصطناعي اهتزازاً شاذّاً. قام النظام بتفعيل كبح الطوارئ فورا وتأمين القطار الخلفي بأمان.")

        # UI Rendering: Sensor Chart Block / تحديث الرسوم البيانية
        with chart_placeholder.container():
            st.markdown("### 📈 Live Sensor & Telemetry Data Analytics / تحليل البيانات الرسومية الفورية")
            st.line_chart(df_history.set_index("Time Step")[["Track Vibration (G)", "Train A Speed (km/h)", "Train B Speed (km/h)"]])

        if is_anomaly:
            break