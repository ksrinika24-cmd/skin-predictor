from __future__ import annotations

from pathlib import Path

import streamlit as st

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "models" / "skin_classifier.onnx"
LABEL_PATH = BASE_DIR / "models" / "labels.txt"
LABELS_PATH = BASE_DIR / "models" / "labels.json"

APP_NAME = "Skin Predictor"
APP_VERSION = "2.0"

PALETTE = {
    "primary": "#6C63FF",
    "secondary": "#FF7EB3",
    "accent": "#7ED957",
    "warning": "#FFC857",
    "danger": "#FF5C8A",
    "bg": "#F7F8FF",
    "dark_bg": "#1E1F2E",
}

SKIN_COLORS = {
    "Normal": PALETTE["accent"],
    "Dry": "#65B7FF",
    "Oily": PALETTE["warning"],
    "Combination": PALETTE["primary"],
    "Sensitive": PALETTE["danger"],
}

LANGUAGES = ["English", "Hindi", "Telugu", "Tamil"]

TRANSLATIONS: dict[str, dict[str, str]] = {
    "English": {},
    "Hindi": {
        "AI Powered Skin Analysis": "एआई संचालित त्वचा विश्लेषण", "Home": "होम", "Skin Analysis": "त्वचा विश्लेषण",
        "Recommendations": "सिफारिशें", "Report": "रिपोर्ट", "About": "परिचय", "Theme": "थीम", "Language": "भाषा",
        "Light": "लाइट", "Dark": "डार्क", "Version": "संस्करण", "Made with": "प्यार से बनाया गया", "Offline AI": "ऑफलाइन एआई",
        "Start Analysis": "विश्लेषण शुरू करें", "Learn More": "और जानें", "Analyze Skin": "त्वचा विश्लेषण करें",
        "Detected Skin Type": "पहचाना गया त्वचा प्रकार", "Confidence": "विश्वास", "Skin Health Score": "त्वचा स्वास्थ्य स्कोर",
        "Morning Routine": "सुबह की दिनचर्या", "Night Routine": "रात की दिनचर्या", "Weekly Routine": "साप्ताहिक दिनचर्या", "Download PDF": "पीडीएफ डाउनलोड करें",
        "Skin Concerns": "त्वचा संबंधी चिंताएं", "Severity": "गंभीरता",
        "Skin Predictor": "स्किन प्रेडिक्टर", "Analyze facial skin using AI completely offline.": "एआई से चेहरे की त्वचा का विश्लेषण पूरी तरह ऑफलाइन करें.",
        "Receive personalized skincare recommendations and professional PDF reports while keeping your image on this device.": "आपकी छवि इसी डिवाइस पर रखते हुए व्यक्तिगत स्किनकेयर सुझाव और पेशेवर पीडीएफ रिपोर्ट पाएं.",
        "Platform Snapshot": "प्लेटफॉर्म झलक", "AI Powered": "एआई संचालित", "Offline ONNX CPU pipeline": "ऑफलाइन ओएनएनएक्स सीपीयू पाइपलाइन",
        "Fast Prediction": "तेज अनुमान", "Optimized image preprocessing": "अनुकूलित छवि तैयारी", "Privacy First": "गोपनीयता पहले",
        "No image upload to cloud": "क्लाउड पर कोई छवि अपलोड नहीं", "Offline": "ऑफलाइन", "Works without internet": "इंटरनेट के बिना काम करता है",
        "What You Can Do": "आप क्या कर सकते हैं", "Upload Image": "छवि अपलोड करें", "Start from PNG, JPEG, JPG, or camera capture.": "पीएनजी, जेपीईजी, जेपीजी या कैमरा कैप्चर से शुरू करें.",
        "AI Detection": "एआई पहचान", "Predict Normal, Dry, Oily, Combination, or Sensitive skin.": "सामान्य, सूखी, तैलीय, मिश्रित या संवेदनशील त्वचा पहचानें.",
        "Product Suggestions": "उत्पाद सुझाव", "Turn prediction output into a practical routine.": "अनुमान को व्यावहारिक दिनचर्या में बदलें.",
        "PDF Report": "पीडीएफ रिपोर्ट", "Generate a branded hospital-style AI report.": "ब्रांडेड हॉस्पिटल-स्टाइल एआई रिपोर्ट बनाएं.",
        "Confidence Analysis": "विश्वास विश्लेषण", "Review confidence, runtime, device, and model metadata.": "विश्वास, रनटाइम, डिवाइस और मॉडल जानकारी देखें.",
        "Skin Care Tips": "त्वचा देखभाल टिप्स", "Get lifestyle and ingredient guidance for your skin type.": "अपनी त्वचा के लिए जीवनशैली और सामग्री मार्गदर्शन पाएं.",
        "Open Skin Analysis from the sidebar to begin.": "शुरू करने के लिए साइडबार से त्वचा विश्लेषण खोलें.",
        "Use a clear front-facing image. The AI pipeline runs locally on CPU and never sends your image outside this app.": "साफ सामने की छवि उपयोग करें. एआई पाइपलाइन स्थानीय सीपीयू पर चलती है और आपकी छवि ऐप से बाहर नहीं भेजती.",
        "Upload. Scan. Understand.": "अपलोड करें. स्कैन करें. समझें.", "Drag & Drop Facial Image": "चेहरे की छवि खींचकर डालें", "Supported formats: PNG, JPEG, JPG": "समर्थित प्रारूप: PNG, JPEG, JPG",
        "Upload image": "छवि अपलोड करें", "Webcam Capture": "वेबकैम कैप्चर", "Image Comparison": "छवि तुलना", "Optional: add a second image for visual comparison.": "वैकल्पिक: दृश्य तुलना के लिए दूसरी छवि जोड़ें.",
        "Comparison image": "तुलना छवि", "Reset Analysis": "विश्लेषण रीसेट करें", "Analysis reset.": "विश्लेषण रीसेट हुआ.", "Primary Image": "मुख्य छवि",
        "Comparison Image": "तुलना छवि", "AI Readiness": "एआई तैयारी", "Image loaded successfully. Start the scan to generate prediction metadata, confidence, skin score, and recommendations.": "छवि सफलतापूर्वक लोड हुई. अनुमान जानकारी, विश्वास, त्वचा स्कोर और सुझाव पाने के लिए स्कैन शुरू करें.",
        "AI is analyzing your skin...": "एआई आपकी त्वचा का विश्लेषण कर रहा है...", "Scanning image...": "छवि स्कैन हो रही है...", "Extracting features...": "विशेषताएं निकाली जा रही हैं...",
        "Running ONNX Model...": "ONNX मॉडल चल रहा है...", "Predicting skin type...": "त्वचा प्रकार का अनुमान हो रहा है...", "Prediction complete.": "अनुमान पूरा हुआ.", "Analysis complete!": "विश्लेषण पूरा हुआ!",
        "Unable to process image. Please try another file.": "छवि संसाधित नहीं हो सकी. कृपया दूसरी फ़ाइल आजमाएं.", "AI Result Dashboard": "एआई परिणाम डैशबोर्ड",
        "Prediction ID": "अनुमान आईडी", "Model Metadata": "मॉडल जानकारी", "Prediction Time": "अनुमान समय", "Model Name": "मॉडल नाम", "Inference Device": "इन्फरेंस डिवाइस",
        "Image Resolution": "छवि रिज़ॉल्यूशन", "Face Detection Status": "चेहरा पहचान स्थिति", "AI Version": "एआई संस्करण", "Provider": "प्रदाता",
        "Skin Analysis Charts": "त्वचा विश्लेषण चार्ट", "Prediction History": "अनुमान इतिहास", "Upload or capture an image to begin.": "शुरू करने के लिए छवि अपलोड या कैप्चर करें.",
        "Analyze your skin first.": "पहले अपनी त्वचा का विश्लेषण करें.", "Skin Care Plan": "त्वचा देखभाल योजना", "Generated using AI based on your detected skin type.": "आपके पहचाने गए त्वचा प्रकार के आधार पर एआई से बनाया गया.",
        "AI recommends this for your skin profile.": "एआई इसे आपकी त्वचा प्रोफाइल के लिए सुझाता है.", "Ingredient Strategy": "सामग्री रणनीति", "Use": "उपयोग करें", "Avoid": "बचें",
        "Lifestyle, Diet, and Dermatologist Advice": "जीवनशैली, आहार और त्वचा विशेषज्ञ सलाह", "Lifestyle Tips": "जीवनशैली टिप्स", "Common Skin Problems": "सामान्य त्वचा समस्याएं",
        "Do's": "क्या करें", "Don'ts": "क्या न करें", "Dermatologist Advice": "त्वचा विशेषज्ञ सलाह", "Product Recommendations": "उत्पाद सुझाव",
        "Category": "श्रेणी", "Description": "विवरण", "Benefits": "लाभ", "Usage": "उपयोग", "Copy Recommendations": "सिफारिशें कॉपी करें",
        "Patient Summary": "रोगी सारांश", "Date": "तारीख", "Time": "समय", "Health Score": "स्वास्थ्य स्कोर", "Model Version": "मॉडल संस्करण", "CPU Runtime": "सीपीयू रनटाइम", "Inference Time": "इन्फरेंस समय",
        "Skin Analysis": "त्वचा विश्लेषण", "Skin Type": "त्वचा प्रकार", "Oil Level": "तेल स्तर", "Hydration Level": "हाइड्रेशन स्तर", "Sensitivity Level": "संवेदनशीलता स्तर", "Texture": "बनावट",
        "AI Explanation": "एआई स्पष्टीकरण", "Characteristics": "विशेषताएं", "Risk Assessment": "जोखिम आकलन", "Risk": "जोखिम", "Recommended Routine": "सुझाई गई दिनचर्या",
        "Recommended Ingredients": "सुझाई गई सामग्री", "Lifestyle Advice": "जीवनशैली सलाह", "Products Included in PDF": "पीडीएफ में शामिल उत्पाद", "Medical Disclaimer": "चिकित्सा अस्वीकरण",
        "This report is AI-generated and intended for informational purposes only. It is not a medical diagnosis or a substitute for consultation with a licensed dermatologist.": "यह रिपोर्ट एआई द्वारा बनाई गई है और केवल जानकारी के लिए है. यह चिकित्सा निदान या लाइसेंस प्राप्त त्वचा विशेषज्ञ की सलाह का विकल्प नहीं है.",
        "Download Premium PDF": "प्रीमियम पीडीएफ डाउनलोड करें", "PDF generation is unavailable. Please install reportlab: pip install reportlab": "पीडीएफ बनाना उपलब्ध नहीं है. कृपया reportlab इंस्टॉल करें: pip install reportlab",
        "About Skin Predictor": "स्किन प्रेडिक्टर के बारे में", "Offline AI for Everyday Skincare": "रोजमर्रा की त्वचा देखभाल के लिए ऑफलाइन एआई",
        "Skin Predictor turns a facial image into skin type insights, practical routines, and polished reports without requiring cloud upload.": "स्किन प्रेडिक्टर क्लाउड अपलोड के बिना चेहरे की छवि को त्वचा जानकारी, दिनचर्या और रिपोर्ट में बदलता है.",
        "Mission, Vision, and Privacy": "मिशन, विजन और गोपनीयता", "Mission": "मिशन", "Make skin analysis private, accessible, and easy to understand for everyone.": "त्वचा विश्लेषण को निजी, सुलभ और सभी के लिए आसान बनाना.",
        "Vision": "विजन", "A responsible AI skincare assistant that helps users build consistent routines and better conversations with dermatology professionals.": "जिम्मेदार एआई स्किनकेयर सहायक जो नियमित दिनचर्या और विशेषज्ञों से बेहतर बातचीत में मदद करे.",
        "Privacy": "गोपनीयता", "Inference runs on the local CPU using ONNX Runtime.": "ONNX Runtime से स्थानीय सीपीयू पर इन्फरेंस चलता है.",
        "Image Control": "छवि नियंत्रण", "Uploaded and captured images are not sent to cloud APIs.": "अपलोड और कैप्चर की गई छवियां क्लाउड एपीआई को नहीं भेजी जातीं.",
        "Local Reports": "स्थानीय रिपोर्ट", "PDF reports are generated inside the app session.": "पीडीएफ रिपोर्ट ऐप सत्र में ही बनती हैं.",
        "Technology Stack": "टेक्नोलॉजी स्टैक", "AI Workflow": "एआई कार्यप्रवाह", "Detection": "पहचान", "Prediction": "अनुमान", "Developer": "निर्माता",
        "Built for Innovation": "नवाचार के लिए बनाया गया", "Designed as a portfolio-ready AI healthcare product with privacy-first offline inference.": "गोपनीयता-प्रथम ऑफलाइन इन्फरेंस वाला पोर्टफोलियो-तैयार एआई हेल्थकेयर उत्पाद.",
        "Contact": "संपर्क", "Future Roadmap": "भविष्य की योजना", "Model Calibration": "मॉडल कैलिब्रेशन", "Continuous validation across more lighting and skin-tone conditions.": "अधिक रोशनी और त्वचा टोन स्थितियों में निरंतर सत्यापन.",
        "Routine Tracking": "दिनचर्या ट्रैकिंग", "Progress history for routines, ingredients, and skin scores.": "दिनचर्या, सामग्री और त्वचा स्कोर का प्रगति इतिहास.",
        "Expanded Concerns": "विस्तृत चिंताएं", "Dedicated signals for acne, pigmentation, redness, and texture.": "मुंहासे, पिगमेंटेशन, लालिमा और बनावट के लिए अलग संकेत.",
        "Clinician Mode": "क्लिनिशियन मोड", "Cleaner exports for consultations with dermatology professionals.": "त्वचा विशेषज्ञों से परामर्श के लिए साफ एक्सपोर्ट.",
        "Normal": "सामान्य", "Dry": "सूखी", "Oily": "तैलीय", "Combination": "मिश्रित", "Sensitive": "संवेदनशील",
    },
    "Telugu": {
        "AI Powered Skin Analysis": "ఏఐ ఆధారిత చర్మ విశ్లేషణ", "Home": "హోమ్", "Skin Analysis": "చర్మ విశ్లేషణ",
        "Recommendations": "సిఫార్సులు", "Report": "రిపోర్ట్", "About": "గురించి", "Theme": "థీమ్", "Language": "భాష",
        "Light": "లైట్", "Dark": "డార్క్", "Version": "వెర్షన్", "Made with": "ప్రేమతో తయారు చేయబడింది", "Offline AI": "ఆఫ్‌లైన్ ఏఐ",
        "Start Analysis": "విశ్లేషణ ప్రారంభించండి", "Learn More": "మరింత తెలుసుకోండి", "Analyze Skin": "చర్మాన్ని విశ్లేషించండి", "Detected Skin Type": "గుర్తించబడిన చర్మ రకం",
        "Morning Routine": "ఉదయ రొటైన్", "Night Routine": "రాత్రి రొటైన్", "Weekly Routine": "వారానికి రొటైన్", "Download PDF": "పిడిఎఫ్ డౌన్‌లోడ్ చేయండి",
        "Confidence": "నమ్మకం", "Skin Health Score": "చర్మ ఆరోగ్య స్కోరు", "Skin Concerns": "చర్మ సమస్యలు", "Severity": "తీవ్రత",
        "Skin Predictor": "స్కిన్ ప్రెడిక్టర్", "Analyze facial skin using AI completely offline.": "ఏఐతో ముఖ చర్మాన్ని పూర్తిగా ఆఫ్‌లైన్‌లో విశ్లేషించండి.",
        "Receive personalized skincare recommendations and professional PDF reports while keeping your image on this device.": "మీ చిత్రం ఈ పరికరంలోనే ఉండగా వ్యక్తిగత చర్మ సంరక్షణ సూచనలు మరియు ప్రొఫెషనల్ PDF రిపోర్టులు పొందండి.",
        "Platform Snapshot": "ప్లాట్‌ఫారమ్ సారాంశం", "AI Powered": "ఏఐ ఆధారితం", "Fast Prediction": "వేగవంతమైన అంచనా", "Privacy First": "గోప్యత ముందుగా",
        "Offline": "ఆఫ్‌లైన్", "Works without internet": "ఇంటర్నెట్ లేకుండా పనిచేస్తుంది", "What You Can Do": "మీరు చేయగలవి", "Upload Image": "చిత్రం అప్లోడ్ చేయండి",
        "AI Detection": "ఏఐ గుర్తింపు", "Product Suggestions": "ఉత్పత్తి సూచనలు", "PDF Report": "PDF రిపోర్ట్", "Confidence Analysis": "నమ్మకం విశ్లేషణ", "Skin Care Tips": "చర్మ సంరక్షణ చిట్కాలు",
        "Open Skin Analysis from the sidebar to begin.": "ప్రారంభించడానికి సైడ్‌బార్‌లో చర్మ విశ్లేషణను తెరవండి.", "Upload. Scan. Understand.": "అప్లోడ్ చేయండి. స్కాన్ చేయండి. అర్థం చేసుకోండి.",
        "Drag & Drop Facial Image": "ముఖ చిత్రాన్ని డ్రాగ్ చేసి డ్రాప్ చేయండి", "Supported formats: PNG, JPEG, JPG": "మద్దతు ఉన్న ఫార్మాట్లు: PNG, JPEG, JPG",
        "Upload image": "చిత్రం అప్లోడ్ చేయండి", "Webcam Capture": "వెబ్‌క్యామ్ క్యాప్చర్", "Image Comparison": "చిత్ర పోలిక", "Comparison image": "పోలిక చిత్రం", "Reset Analysis": "విశ్లేషణ రీసెట్ చేయండి",
        "Primary Image": "ప్రధాన చిత్రం", "Comparison Image": "పోలిక చిత్రం", "AI Readiness": "ఏఐ సిద్ధత", "Analyze your skin first.": "ముందుగా మీ చర్మాన్ని విశ్లేషించండి.",
        "Prediction complete.": "అంచనా పూర్తయింది.", "Analysis complete!": "విశ్లేషణ పూర్తయింది!", "AI Result Dashboard": "ఏఐ ఫలితాల డ్యాష్‌బోర్డ్", "Prediction ID": "అంచనా ఐడి",
        "Model Metadata": "మోడల్ వివరాలు", "Prediction Time": "అంచనా సమయం", "Model Name": "మోడల్ పేరు", "Inference Device": "ఇన్ఫరెన్స్ పరికరం", "Image Resolution": "చిత్ర రిజల్యూషన్",
        "Face Detection Status": "ముఖ గుర్తింపు స్థితి", "AI Version": "ఏఐ వెర్షన్", "Provider": "ప్రొవైడర్", "Skin Analysis Charts": "చర్మ విశ్లేషణ చార్ట్లు",
        "Prediction History": "అంచనా చరిత్ర", "Upload or capture an image to begin.": "ప్రారంభించడానికి చిత్రం అప్లోడ్ లేదా క్యాప్చర్ చేయండి.",
        "Skin Care Plan": "చర్మ సంరక్షణ ప్రణాళిక", "Generated using AI based on your detected skin type.": "మీ గుర్తించిన చర్మ రకం ఆధారంగా ఏఐతో రూపొందించబడింది.",
        "Ingredient Strategy": "పదార్థాల వ్యూహం", "Use": "వాడండి", "Avoid": "నివారించండి", "Lifestyle, Diet, and Dermatologist Advice": "జీవనశైలి, ఆహారం మరియు చర్మ వైద్యుల సలహా",
        "Lifestyle Tips": "జీవనశైలి చిట్కాలు", "Common Skin Problems": "సాధారణ చర్మ సమస్యలు", "Do's": "చేయాల్సినవి", "Don'ts": "చేయకూడనివి", "Dermatologist Advice": "చర్మ వైద్యుల సలహా",
        "Product Recommendations": "ఉత్పత్తి సూచనలు", "Category": "వర్గం", "Description": "వివరణ", "Benefits": "లాభాలు", "Usage": "వినియోగం", "Copy Recommendations": "సిఫార్సులను కాపీ చేయండి",
        "Patient Summary": "రోగి సారాంశం", "Date": "తేదీ", "Time": "సమయం", "Health Score": "ఆరోగ్య స్కోరు", "Model Version": "మోడల్ వెర్షన్", "CPU Runtime": "CPU రన్‌టైమ్", "Inference Time": "ఇన్ఫరెన్స్ సమయం",
        "Skin Type": "చర్మ రకం", "Oil Level": "నూనె స్థాయి", "Hydration Level": "తేమ స్థాయి", "Sensitivity Level": "సున్నితత్వ స్థాయి", "Texture": "నిర్మాణం", "AI Explanation": "ఏఐ వివరణ",
        "Characteristics": "లక్షణాలు", "Risk Assessment": "రిస్క్ అంచనా", "Risk": "రిస్క్", "Recommended Routine": "సిఫార్సు చేసిన రొటీన్", "Recommended Ingredients": "సిఫార్సు చేసిన పదార్థాలు",
        "Lifestyle Advice": "జీవనశైలి సలహా", "Products Included in PDF": "PDFలో ఉన్న ఉత్పత్తులు", "Medical Disclaimer": "వైద్య నిరాకరణ", "Download Premium PDF": "ప్రీమియం PDF డౌన్‌లోడ్ చేయండి",
        "About Skin Predictor": "స్కిన్ ప్రెడిక్టర్ గురించి", "Offline AI for Everyday Skincare": "రోజువారీ చర్మ సంరక్షణకు ఆఫ్‌లైన్ ఏఐ", "Mission, Vision, and Privacy": "మిషన్, విజన్ మరియు గోప్యత",
        "Mission": "మిషన్", "Vision": "విజన్", "Privacy": "గోప్యత", "Image Control": "చిత్ర నియంత్రణ", "Local Reports": "స్థానిక రిపోర్టులు", "Technology Stack": "టెక్నాలజీ స్టాక్",
        "AI Workflow": "ఏఐ వర్క్‌ఫ్లో", "Detection": "గుర్తింపు", "Prediction": "అంచనా", "Developer": "నిర్మాత", "Built for Innovation": "ఆవిష్కరణ కోసం నిర్మించబడింది",
        "Contact": "సంప్రదించండి", "Future Roadmap": "భవిష్యత్ రోడ్‌మ్యాప్", "Model Calibration": "మోడల్ కాలిబ్రేషన్", "Routine Tracking": "రొటీన్ ట్రాకింగ్", "Expanded Concerns": "విస్తరించిన సమస్యలు",
        "Clinician Mode": "క్లినిషియన్ మోడ్", "Normal": "సాధారణ", "Dry": "పొడి", "Oily": "నూనెగల", "Combination": "మిశ్రమ", "Sensitive": "సున్నితమైన",
    },
    "Tamil": {
        "AI Powered Skin Analysis": "ஏஐ தோல் பகுப்பாய்வு", "Home": "முகப்பு", "Skin Analysis": "தோல் பகுப்பாய்வு",
        "Recommendations": "பரிந்துரைகள்", "Report": "அறிக்கை", "About": "பற்றி", "Theme": "தீம்", "Language": "மொழி",
        "Light": "லைட்", "Dark": "டார்க்", "Version": "பதிப்பு", "Made with": "அன்புடன் உருவாக்கப்பட்டது", "Offline AI": "ஆஃப்லைன் ஏஐ",
        "Start Analysis": "பகுப்பாய்வு தொடங்கு", "Learn More": "மேலும் அறிக", "Analyze Skin": "தோலை பகுப்பாய்வு செய்", "Detected Skin Type": "கண்டறியப்பட்ட தோல் வகை",
        "Morning Routine": "காலை நடைமுறை", "Night Routine": "இரவு நடைமுறை", "Weekly Routine": "வாராந்திர நடைமுறை", "Download PDF": "PDF பதிவிறக்கவும்",
        "Confidence": "நம்பிக்கை", "Skin Health Score": "தோல் ஆரோக்கிய மதிப்பெண்", "Skin Concerns": "தோல் கவலைகள்", "Severity": "தீவிரம்",
        "Skin Predictor": "ஸ்கின் பிரெடிக்டர்", "Analyze facial skin using AI completely offline.": "ஏஐ மூலம் முகத் தோலை முழுமையாக ஆஃப்லைனில் பகுப்பாய்வு செய்யுங்கள்.",
        "Receive personalized skincare recommendations and professional PDF reports while keeping your image on this device.": "உங்கள் படம் இச்சாதனத்திலேயே இருக்கும் நிலையில் தனிப்பயன் தோல் பராமரிப்பு பரிந்துரைகள் மற்றும் PDF அறிக்கைகளை பெறுங்கள்.",
        "Platform Snapshot": "தள சுருக்கம்", "AI Powered": "ஏஐ இயக்கம்", "Fast Prediction": "வேகமான கணிப்பு", "Privacy First": "தனியுரிமை முதலில்",
        "Offline": "ஆஃப்லைன்", "Works without internet": "இணையம் இல்லாமல் இயங்கும்", "What You Can Do": "நீங்கள் செய்யக்கூடியவை", "Upload Image": "படத்தை பதிவேற்று",
        "AI Detection": "ஏஐ கண்டறிதல்", "Product Suggestions": "தயாரிப்பு பரிந்துரைகள்", "PDF Report": "PDF அறிக்கை", "Confidence Analysis": "நம்பிக்கை பகுப்பாய்வு", "Skin Care Tips": "தோல் பராமரிப்பு குறிப்புகள்",
        "Open Skin Analysis from the sidebar to begin.": "தொடங்க சைட்பாரில் தோல் பகுப்பாய்வைத் திறக்கவும்.", "Upload. Scan. Understand.": "பதிவேற்று. ஸ்கேன் செய். புரிந்துகொள்.",
        "Drag & Drop Facial Image": "முகப் படத்தை இழுத்து விடுங்கள்", "Supported formats: PNG, JPEG, JPG": "ஆதரவு வடிவங்கள்: PNG, JPEG, JPG",
        "Upload image": "படத்தை பதிவேற்று", "Webcam Capture": "வெப்கேம் பிடிப்பு", "Image Comparison": "பட ஒப்பீடு", "Comparison image": "ஒப்பீட்டு படம்", "Reset Analysis": "பகுப்பாய்வை மீட்டமை",
        "Primary Image": "முதன்மை படம்", "Comparison Image": "ஒப்பீட்டு படம்", "AI Readiness": "ஏஐ தயார்நிலை", "Analyze your skin first.": "முதலில் உங்கள் தோலை பகுப்பாய்வு செய்யுங்கள்.",
        "Prediction complete.": "கணிப்பு முடிந்தது.", "Analysis complete!": "பகுப்பாய்வு முடிந்தது!", "AI Result Dashboard": "ஏஐ முடிவு பலகை", "Prediction ID": "கணிப்பு ஐடி",
        "Model Metadata": "மாதிரி விவரங்கள்", "Prediction Time": "கணிப்பு நேரம்", "Model Name": "மாதிரி பெயர்", "Inference Device": "இன்ஃபரன்ஸ் சாதனம்", "Image Resolution": "பட தீர்மானம்",
        "Face Detection Status": "முக கண்டறிதல் நிலை", "AI Version": "ஏஐ பதிப்பு", "Provider": "வழங்குபவர்", "Skin Analysis Charts": "தோல் பகுப்பாய்வு வரைபடங்கள்",
        "Prediction History": "கணிப்பு வரலாறு", "Upload or capture an image to begin.": "தொடங்க படத்தை பதிவேற்றவும் அல்லது பிடிக்கவும்.",
        "Skin Care Plan": "தோல் பராமரிப்பு திட்டம்", "Generated using AI based on your detected skin type.": "கண்டறியப்பட்ட தோல் வகையை அடிப்படையாகக் கொண்டு ஏஐ மூலம் உருவாக்கப்பட்டது.",
        "Ingredient Strategy": "பொருள் திட்டம்", "Use": "பயன்படுத்து", "Avoid": "தவிர்", "Lifestyle, Diet, and Dermatologist Advice": "வாழ்க்கை முறை, உணவு மற்றும் தோல் மருத்துவர் ஆலோசனை",
        "Lifestyle Tips": "வாழ்க்கை முறை குறிப்புகள்", "Common Skin Problems": "பொதுவான தோல் பிரச்சனைகள்", "Do's": "செய்யவேண்டியவை", "Don'ts": "செய்யக்கூடாதவை", "Dermatologist Advice": "தோல் மருத்துவர் ஆலோசனை",
        "Product Recommendations": "தயாரிப்பு பரிந்துரைகள்", "Category": "வகை", "Description": "விளக்கம்", "Benefits": "நன்மைகள்", "Usage": "பயன்பாடு", "Copy Recommendations": "பரிந்துரைகளை நகலெடு",
        "Patient Summary": "நோயாளர் சுருக்கம்", "Date": "தேதி", "Time": "நேரம்", "Health Score": "ஆரோக்கிய மதிப்பெண்", "Model Version": "மாதிரி பதிப்பு", "CPU Runtime": "CPU இயக்க நேரம்", "Inference Time": "இன்ஃபரன்ஸ் நேரம்",
        "Skin Type": "தோல் வகை", "Oil Level": "எண்ணெய் நிலை", "Hydration Level": "ஈரப்பத நிலை", "Sensitivity Level": "உணர்திறன் நிலை", "Texture": "அமைப்பு", "AI Explanation": "ஏஐ விளக்கம்",
        "Characteristics": "அம்சங்கள்", "Risk Assessment": "ஆபத்து மதிப்பீடு", "Risk": "ஆபத்து", "Recommended Routine": "பரிந்துரைக்கப்பட்ட நடைமுறை", "Recommended Ingredients": "பரிந்துரைக்கப்பட்ட பொருட்கள்",
        "Lifestyle Advice": "வாழ்க்கை முறை ஆலோசனை", "Products Included in PDF": "PDFல் உள்ள தயாரிப்புகள்", "Medical Disclaimer": "மருத்துவ மறுப்பு", "Download Premium PDF": "பிரீமியம் PDF பதிவிறக்கவும்",
        "About Skin Predictor": "ஸ்கின் பிரெடிக்டர் பற்றி", "Offline AI for Everyday Skincare": "தினசரி தோல் பராமரிப்புக்கு ஆஃப்லைன் ஏஐ", "Mission, Vision, and Privacy": "பணி, பார்வை மற்றும் தனியுரிமை",
        "Mission": "பணி", "Vision": "பார்வை", "Privacy": "தனியுரிமை", "Image Control": "பட கட்டுப்பாடு", "Local Reports": "உள்ளூர் அறிக்கைகள்", "Technology Stack": "தொழில்நுட்ப அடுக்கு",
        "AI Workflow": "ஏஐ பணிப்பாய்வு", "Detection": "கண்டறிதல்", "Prediction": "கணிப்பு", "Developer": "உருவாக்கம்", "Built for Innovation": "புதுமைக்காக உருவாக்கப்பட்டது",
        "Contact": "தொடர்பு", "Future Roadmap": "எதிர்கால திட்டம்", "Model Calibration": "மாதிரி ஒத்திசைவு", "Routine Tracking": "நடைமுறை கண்காணிப்பு", "Expanded Concerns": "விரிவான கவலைகள்",
        "Clinician Mode": "மருத்துவர் முறை", "Normal": "சாதாரண", "Dry": "உலர்", "Oily": "எண்ணெய்", "Combination": "கலப்பு", "Sensitive": "உணர்திறன்",
    },
}

TRANSLATIONS["Hindi"].update({
    "Analyze your facial skin using Artificial Intelligence and receive personalized skincare recommendations tailored to your skin type.": "कृत्रिम बुद्धिमत्ता से अपने चेहरे की त्वचा का विश्लेषण करें और अपनी त्वचा के प्रकार के अनुसार व्यक्तिगत स्किनकेयर सुझाव पाएं.",
    "Why Choose Skin Predictor": "स्किन प्रेडिक्टर क्यों चुनें", "Local offline intelligence": "स्थानीय ऑफलाइन बुद्धिमत्ता", "Fast": "तेज", "Seconds to results": "सेकंडों में परिणाम", "Secure": "सुरक्षित", "No cloud upload": "कोई क्लाउड अपलोड नहीं", "Private": "निजी", "Your data stays local": "आपका डेटा स्थानीय रहता है", "Quick": "त्वरित", "Instant analysis": "तुरंत विश्लेषण", "Accurate": "सटीक", "Dermatologist inspired": "त्वचा विशेषज्ञों से प्रेरित", "Dermatologist Inspired": "त्वचा विशेषज्ञ प्रेरित", "Medically reviewed": "चिकित्सकीय रूप से समीक्षा की गई",
    "How It Works": "यह कैसे काम करता है", "AI Analysis": "एआई विश्लेषण", "Skin Detection": "त्वचा पहचान", "Download Report": "रिपोर्ट डाउनलोड करें", "Features": "सुविधाएं", "PNG, JPEG, JPG, or camera capture": "PNG, JPEG, JPG या कैमरा कैप्चर", "Predict Normal, Dry, Oily, Combination, or Sensitive skin": "सामान्य, सूखी, तैलीय, मिश्रित या संवेदनशील त्वचा का अनुमान", "Personalized skincare routine": "व्यक्तिगत त्वचा देखभाल दिनचर्या", "Professional hospital-style report": "पेशेवर अस्पताल-शैली रिपोर्ट", "View detailed metrics": "विस्तृत मेट्रिक्स देखें", "Ingredient and lifestyle guidance": "सामग्री और जीवनशैली मार्गदर्शन",
    "What Users Say": "उपयोगकर्ता क्या कहते हैं", "This app helped me understand my skin type better!": "इस ऐप ने मेरी त्वचा का प्रकार बेहतर समझने में मदद की!", "Amazing offline analysis, very accurate.": "शानदार ऑफलाइन विश्लेषण, बहुत सटीक.", "Love the personalized recommendations.": "व्यक्तिगत सुझाव बहुत पसंद आए.", "FAQ": "अक्सर पूछे जाने वाले प्रश्न", "How accurate is the AI analysis?": "एआई विश्लेषण कितना सटीक है?", "Our AI model achieves 85-95% accuracy on diverse skin types.": "हमारा एआई मॉडल विविध त्वचा प्रकारों पर 85-95% सटीकता प्राप्त करता है.", "Is my image stored or uploaded?": "क्या मेरी छवि संग्रहीत या अपलोड होती है?", "No, all processing happens locally on your device.": "नहीं, पूरी प्रक्रिया आपके डिवाइस पर स्थानीय रूप से होती है.", "Do I need internet connection?": "क्या इंटरनेट कनेक्शन चाहिए?", "No, the app works completely offline.": "नहीं, ऐप पूरी तरह ऑफलाइन काम करता है.", "Privacy Policy": "गोपनीयता नीति",
    "Size": "आकार", "Resolution": "रिज़ॉल्यूशन", "Upload time": "अपलोड समय", "confidence": "विश्वास", "No report available. Analyze your skin first.": "कोई रिपोर्ट उपलब्ध नहीं है. पहले त्वचा का विश्लेषण करें.", "Skin Report": "त्वचा रिपोर्ट", "Routine": "दिनचर्या", "Morning": "सुबह", "Night": "रात", "Weekly": "साप्ताहिक", "Lifestyle": "जीवनशैली", "Products": "उत्पाद", "Model": "मॉडल", "Sensitivity": "संवेदनशीलता", "Concerns": "चिंताएं", "Generated by": "द्वारा निर्मित", "on": "को", "AI Powered Skin Analysis Report": "एआई संचालित त्वचा विश्लेषण रिपोर्ट",
    "Low": "कम", "Medium": "मध्यम", "High": "अधिक", "Low-Medium": "कम-मध्यम", "Balanced": "संतुलित", "Healthy": "स्वस्थ", "Mixed": "मिश्रित", "Variable": "परिवर्तनीय", "T-zone high": "टी-ज़ोन अधिक", "Even and resilient": "समान और मजबूत", "Tight or flaky": "तनावयुक्त या परतदार", "Shiny with visible pores": "चमकदार और स्पष्ट रोमछिद्र", "Oily center with drier cheeks": "बीच में तैलीय और गाल सूखे", "Reactive or redness prone": "प्रतिक्रियाशील या लालिमा-प्रवण",
    "Acne": "मुंहासे", "Pigmentation": "पिगमेंटेशन", "Sun Damage": "धूप से नुकसान", "Dryness": "सूखापन", "Mild dullness": "हल्की फीकी त्वचा", "Sun protection": "धूप से सुरक्षा", "Flakiness": "परतदारपन", "Barrier weakness": "बैरियर कमजोरी", "Fine lines": "बारीक रेखाएं", "Excess sebum": "अधिक सीबम", "Clogged pores": "बंद रोमछिद्र", "Acne risk": "मुंहासों का जोखिम", "T-zone shine": "टी-ज़ोन चमक", "Cheek dryness": "गालों का सूखापन", "Uneven texture": "असमान बनावट", "Redness": "लालिमा", "Irritation": "जलन", "Barrier stress": "बैरियर तनाव",
    "Maintain hydration, antioxidant support, and daily sunscreen.": "हाइड्रेशन, एंटीऑक्सीडेंट समर्थन और दैनिक सनस्क्रीन बनाए रखें.", "Focus on barrier repair, humectants, and richer moisturizers.": "बैरियर मरम्मत, ह्यूमेक्टेंट और गाढ़े मॉइस्चराइज़र पर ध्यान दें.", "Use light hydration, niacinamide, and oil-control actives.": "हल्का हाइड्रेशन, नियासिनामाइड और तेल नियंत्रण एक्टिव्स उपयोग करें.", "Balance oily and dry zones separately with flexible layers.": "तैलीय और सूखे क्षेत्रों को अलग-अलग संतुलित करें.", "Choose calming, fragrance-free products and patch test new actives.": "शांत करने वाले, सुगंध-रहित उत्पाद चुनें और नए एक्टिव्स का पैच टेस्ट करें.",
    "Even tone": "समान टोन", "Balanced oil": "संतुलित तेल", "Good moisture retention": "अच्छी नमी धारण क्षमता", "Tightness": "तनाव", "Fine texture": "महीन बनावट", "Needs barrier support": "बैरियर समर्थन चाहिए", "Shine prone": "चमक की प्रवृत्ति", "Congestion risk": "जमाव का जोखिम", "Benefits from niacinamide": "नियासिनामाइड से लाभ", "Mixed oil levels": "मिश्रित तेल स्तर", "Adaptable routine": "अनुकूलनीय दिनचर्या", "Redness prone": "लालिमा की प्रवृत्ति", "Barrier care needed": "बैरियर देखभाल आवश्यक", "Patch testing recommended": "पैच टेस्ट सुझाया गया",
    "Balanced Oil": "संतुलित तेल", "Hydration": "हाइड्रेशन", "Low Sensitivity": "कम संवेदनशीलता", "Barrier": "बैरियर", "Single face detected": "एक चेहरा मिला", "Multiple faces detected": "कई चेहरे मिले", "No face detected": "चेहरा नहीं मिला", "Face detection unavailable": "चेहरा पहचान उपलब्ध नहीं", "CPU": "सीपीयू", "CPUExecutionProvider": "सीपीयू एक्ज़ीक्यूशन प्रदाता", "ONNX Runtime CPU": "ONNX रनटाइम सीपीयू",
    "AI recommends this for your skin profile.": "एआई आपकी त्वचा प्रोफाइल के लिए यह सुझाता है.", "Simple Refreshing Face Wash": "सरल ताज़गी फेस वॉश", "Vitamin C serum": "विटामिन C सीरम", "Light moisturizer": "हल्का मॉइस्चराइज़र", "Broad spectrum SPF 50": "ब्रॉड स्पेक्ट्रम SPF 50", "Gentle cleanser": "कोमल क्लेंज़र", "Peptide serum": "पेप्टाइड सीरम", "Night cream": "नाइट क्रीम", "Lip balm": "लिप बाम", "Mild exfoliation": "हल्का एक्सफोलिएशन", "Hydrating mask": "हाइड्रेटिंग मास्क", "Scalp and pillowcase hygiene": "स्कैल्प और तकिए की स्वच्छता", "Cream cleanser": "क्रीम क्लेंज़र", "Hyaluronic acid": "हयालूरोनिक एसिड", "Ceramide moisturizer": "सेरामाइड मॉइस्चराइज़र", "SPF 30+": "SPF 30+", "Hydrating face wash": "हाइड्रेटिंग फेस वॉश", "Squalane serum": "स्क्वालेन सीरम", "Rich night cream": "रिच नाइट क्रीम", "Occlusive balm": "ओक्लूसिव बाम", "No harsh scrub": "कठोर स्क्रब नहीं", "Barrier recovery night": "बैरियर रिकवरी नाइट",
    "Niacinamide serum": "नियासिनामाइड सीरम", "Oil-free gel moisturizer": "ऑयल-फ्री जेल मॉइस्चराइज़र", "Matte SPF 50": "मैट SPF 50", "Salicylic cleanser": "सैलिसिलिक क्लेंज़र", "BHA or zinc serum": "BHA या जिंक सीरम", "Light gel cream": "हल्की जेल क्रीम", "Spot care": "स्पॉट केयर", "Clay mask": "क्ले मास्क", "Gentle exfoliation": "कोमल एक्सफोलिएशन", "Non-comedogenic mask": "नॉन-कॉमेडोजेनिक मास्क", "Simple Face Wash": "सिंपल फेस वॉश", "Vitamin C": "विटामिन C", "Light moisturizer on T-zone": "टी-ज़ोन पर हल्का मॉइस्चराइज़र", "Hydrating cream on cheeks": "गालों पर हाइड्रेटिंग क्रीम", "SPF 50": "SPF 50", "Balanced cleanser": "संतुलित क्लेंज़र", "Zone-based moisturizer": "ज़ोन आधारित मॉइस्चराइज़र", "Eye cream": "आई क्रीम", "Clay mask only on T-zone": "क्ले मास्क केवल टी-ज़ोन पर", "Hydrating mask on cheeks": "गालों पर हाइड्रेटिंग मास्क", "Centella serum": "सेंटेला सीरम", "Mineral SPF 50": "मिनरल SPF 50", "Panthenol serum": "पैंथेनॉल सीरम", "Soothing mask": "शांत करने वाला मास्क", "Patch test": "पैच टेस्ट", "Avoid harsh exfoliation": "कठोर एक्सफोलिएशन से बचें",
    "Peptides": "पेप्टाइड्स", "Hyaluronic Acid": "हयालूरोनिक एसिड", "Ceramides": "सेरामाइड्स", "Shea Butter": "शिया बटर", "Squalane": "स्क्वालेन", "Glycerin": "ग्लिसरीन", "Niacinamide": "नियासिनामाइड", "Salicylic Acid": "सैलिसिलिक एसिड", "Clay Mask": "क्ले मास्क", "Oil-Free Moisturizer": "ऑयल-फ्री मॉइस्चराइज़र", "Green Tea": "ग्रीन टी", "Lactic Acid": "लैक्टिक एसिड", "Centella": "सेंटेला", "Panthenol": "पैंथेनॉल",
    "Skipping sunscreen": "सनस्क्रीन छोड़ना", "Over-exfoliation": "अधिक एक्सफोलिएशन", "Sleeping with makeup": "मेकअप लगाकर सोना", "Harsh cleansers": "कठोर क्लेंज़र", "Alcohol toners": "अल्कोहल टोनर", "Frequent exfoliation": "बार-बार एक्सफोलिएशन", "Heavy creams": "भारी क्रीम", "Coconut oil": "नारियल तेल", "Greasy sunscreen": "चिपचिपी सनस्क्रीन", "One-size heavy creams": "एक जैसी भारी क्रीम", "Strong acids all over": "हर जगह तेज़ एसिड", "Skipping moisturizer": "मॉइस्चराइज़र छोड़ना", "Alcohol": "अल्कोहल", "Fragrance": "सुगंध", "Strong acids": "तेज़ एसिड", "High-strength retinol": "उच्च शक्ति रेटिनॉल",
    "2-2.5L water": "2-2.5 लीटर पानी", "7-8 hours sleep": "7-8 घंटे नींद", "Colorful fruits": "रंगीन फल", "30 min movement": "30 मिनट गतिविधि", "2.5-3L water": "2.5-3 लीटर पानी", "Humidify room": "कमरे में नमी रखें", "Omega-3 foods": "ओमेगा-3 भोजन", "Gentle exercise": "हल्का व्यायाम", "2-3L water": "2-3 लीटर पानी", "Low-glycemic meals": "लो-ग्लाइसेमिक भोजन", "Clean phone screen": "फोन स्क्रीन साफ रखें", "Regular workouts": "नियमित व्यायाम", "Balanced diet": "संतुलित आहार", "Sleep schedule": "नींद का समय", "Moderate exercise": "मध्यम व्यायाम", "Stress reduction": "तनाव कम करें", "Simple diet": "सरल आहार", "Sleep 7-8 hours": "7-8 घंटे सोएं",
    "Dullness": "फीकापन", "Occasional dryness": "कभी-कभी सूखापन", "Flaking": "परत उतरना", "Barrier damage": "बैरियर नुकसान", "Blackheads": "ब्लैकहेड्स", "Shine": "चमक", "Texture": "बनावट", "T-zone oil": "टी-ज़ोन तेल", "Stinging": "चुभन", "Maintain routine": "दिनचर्या बनाए रखें", "Use sunscreen daily": "रोज सनस्क्रीन लगाएं", "Do not over-layer actives": "बहुत अधिक एक्टिव्स न लगाएं", "Apply moisturizer on damp skin": "नम त्वचा पर मॉइस्चराइज़र लगाएं", "Use lukewarm water": "गुनगुना पानी उपयोग करें", "Avoid hot showers on face": "चेहरे पर गर्म पानी से बचें", "Use non-comedogenic products": "नॉन-कॉमेडोजेनिक उत्पाद उपयोग करें", "Cleanse twice daily": "दिन में दो बार साफ करें", "Do not strip skin aggressively": "त्वचा को कठोरता से न सुखाएं", "Treat zones separately": "क्षेत्रों को अलग-अलग संभालें", "Use lightweight layers": "हल्की परतें लगाएं", "Do not use drying products on cheeks": "गालों पर सुखाने वाले उत्पाद न लगाएं", "Patch test products": "उत्पादों का पैच टेस्ट करें", "Use fragrance-free care": "सुगंध-रहित देखभाल उपयोग करें", "Do not mix many actives": "कई एक्टिव्स न मिलाएं",
    "Maintain hydration and protection; keep the routine simple and consistent.": "हाइड्रेशन और सुरक्षा बनाए रखें; दिनचर्या सरल और नियमित रखें.", "Repair the moisture barrier first, then add brightening actives slowly.": "पहले नमी बैरियर सुधारें, फिर ब्राइटनिंग एक्टिव्स धीरे जोड़ें.", "Control oil while preserving hydration; stripped skin often becomes oilier.": "हाइड्रेशन बचाते हुए तेल नियंत्रित करें; बहुत सूखी त्वचा और तैलीय हो सकती है.", "Balance oily and dry zones separately instead of forcing one routine everywhere.": "हर जगह एक ही दिनचर्या लगाने के बजाय तैलीय और सूखे क्षेत्रों को अलग संभालें.", "Calm the barrier and introduce one new product at a time.": "बैरियर को शांत करें और एक समय में एक नया उत्पाद जोड़ें.",
    "Face Wash": "फेस वॉश", "Moisturizer": "मॉइस्चराइज़र", "Sunscreen": "सनस्क्रीन", "Serum": "सीरम", "Night Cream": "नाइट क्रीम", "Face Mask": "फेस मास्क", "Toner": "टोनर", "Lip Balm": "लिप बाम", "Eye Cream": "आई क्रीम", "Cleanser": "क्लेंज़र", "Morning and night": "सुबह और रात", "Morning": "सुबह", "Every morning": "हर सुबह", "Night": "रात", "Weekly": "साप्ताहिक", "After cleanse": "साफ करने के बाद", "As needed": "ज़रूरत अनुसार", "Twice daily": "दिन में दो बार", "Before cream": "क्रीम से पहले", "Morning or night": "सुबह या रात", "2-3 nights weekly": "सप्ताह में 2-3 रातें", "Daytime": "दिन में", "Gentle daily cleanse": "कोमल दैनिक सफाई", "Keeps skin balanced": "त्वचा संतुलित रखता है", "Light hydration": "हल्का हाइड्रेशन", "Fresh non-greasy finish": "ताज़ा बिना चिकनाई फिनिश", "Daily UV defense": "दैनिक यूवी सुरक्षा", "Protects tone and texture": "टोन और बनावट की रक्षा", "Antioxidant glow": "एंटीऑक्सीडेंट चमक", "Helps dullness": "फीकेपन में मदद", "Comfort hydration": "आरामदायक हाइड्रेशन", "Softens overnight": "रातभर नरम करता है", "Weekly hydration": "साप्ताहिक हाइड्रेशन", "Boosts glow": "चमक बढ़ाता है", "Light refresh": "हल्की ताज़गी", "Preps skin": "त्वचा तैयार करता है", "Lip barrier": "होंठ बैरियर", "Prevents dryness": "सूखापन रोकता है", "Under-eye care": "आंखों के नीचे देखभाल", "Refreshes tired eyes": "थकी आंखों को ताज़ा करता है", "Recommended skincare option": "सुझाया गया स्किनकेयर विकल्प", "Supports your skin routine": "आपकी त्वचा दिनचर्या में सहायक", "Use as directed": "निर्देशानुसार उपयोग करें"
})

TRANSLATIONS["Telugu"].update({
    "Why Choose Skin Predictor": "స్కిన్ ప్రెడిక్టర్ ఎందుకు?", "How It Works": "ఇది ఎలా పనిచేస్తుంది", "Features": "లక్షణాలు", "What Users Say": "వినియోగదారుల అభిప్రాయాలు", "FAQ": "తరచుగా అడిగే ప్రశ్నలు", "Privacy Policy": "గోప్యతా విధానం", "Size": "పరిమాణం", "Resolution": "రిజల్యూషన్", "Upload time": "అప్లోడ్ సమయం", "confidence": "నమ్మకం", "No report available. Analyze your skin first.": "రిపోర్ట్ లేదు. ముందుగా చర్మాన్ని విశ్లేషించండి.", "Skin Report": "చర్మ రిపోర్ట్", "Routine": "రొటీన్", "Morning": "ఉదయం", "Night": "రాత్రి", "Weekly": "వారానికి", "Lifestyle": "జీవనశైలి", "Products": "ఉత్పత్తులు", "Model": "మోడల్", "Sensitivity": "సున్నితత్వం", "Concerns": "సమస్యలు", "Generated by": "రూపొందించినది", "on": "నాడు", "AI Powered Skin Analysis Report": "ఏఐ ఆధారిత చర్మ విశ్లేషణ రిపోర్ట్",
    "Analyze your facial skin using Artificial Intelligence and receive personalized skincare recommendations tailored to your skin type.": "కృత్రిమ మేధస్సుతో మీ ముఖ చర్మాన్ని విశ్లేషించి, మీ చర్మ రకానికి సరిపోయే వ్యక్తిగత సూచనలు పొందండి.", "Local offline intelligence": "స్థానిక ఆఫ్‌లైన్ మేధస్సు", "Fast": "వేగం", "Seconds to results": "సెకన్లలో ఫలితాలు", "Secure": "సురక్షితం", "No cloud upload": "క్లౌడ్ అప్లోడ్ లేదు", "Private": "ప్రైవేట్", "Your data stays local": "మీ డేటా స్థానికంగానే ఉంటుంది", "Quick": "త్వరితం", "Instant analysis": "తక్షణ విశ్లేషణ", "Accurate": "ఖచ్చితమైనది", "Dermatologist inspired": "చర్మ నిపుణుల ప్రేరణతో", "Dermatologist Inspired": "చర్మ నిపుణుల ప్రేరణతో", "Medically reviewed": "వైద్యపరంగా సమీక్షించబడింది", "AI Analysis": "ఏఐ విశ్లేషణ", "Skin Detection": "చర్మ గుర్తింపు", "Download Report": "రిపోర్ట్ డౌన్‌లోడ్", "PNG, JPEG, JPG, or camera capture": "PNG, JPEG, JPG లేదా కెమెరా క్యాప్చర్", "Predict Normal, Dry, Oily, Combination, or Sensitive skin": "సాధారణ, పొడి, నూనెగల, మిశ్రమ లేదా సున్నిత చర్మాన్ని అంచనా వేయండి", "Personalized skincare routine": "వ్యక్తిగత చర్మ సంరక్షణ రొటీన్", "Professional hospital-style report": "ప్రొఫెషనల్ హాస్పిటల్-స్టైల్ రిపోర్ట్", "View detailed metrics": "వివరమైన మెట్రిక్స్ చూడండి", "Ingredient and lifestyle guidance": "పదార్థాలు మరియు జీవనశైలి మార్గదర్శకం",
    "How accurate is the AI analysis?": "ఏఐ విశ్లేషణ ఎంత ఖచ్చితం?", "Our AI model achieves 85-95% accuracy on diverse skin types.": "మా ఏఐ మోడల్ విభిన్న చర్మ రకాలపై 85-95% ఖచ్చితత్వం ఇస్తుంది.", "Is my image stored or uploaded?": "నా చిత్రం నిల్వ చేయబడుతుందా లేదా అప్లోడ్ అవుతుందా?", "No, all processing happens locally on your device.": "లేదు, మొత్తం ప్రాసెసింగ్ మీ పరికరంలో స్థానికంగా జరుగుతుంది.", "Do I need internet connection?": "ఇంటర్నెట్ అవసరమా?", "No, the app works completely offline.": "లేదు, యాప్ పూర్తిగా ఆఫ్‌లైన్‌లో పనిచేస్తుంది.",
    "Low": "తక్కువ", "Medium": "మధ్యస్థ", "High": "అధికం", "Low-Medium": "తక్కువ-మధ్యస్థ", "Balanced": "సమతుల్యం", "Healthy": "ఆరోగ్యకరం", "Mixed": "మిశ్రమం", "Variable": "మారుతూ ఉండేది", "T-zone high": "టి-జోన్ అధికం", "Acne": "మొటిమలు", "Pigmentation": "పిగ్మెంటేషన్", "Sun Damage": "సూర్య నష్టం", "Dryness": "పొడితనం", "Mild dullness": "స్వల్ప మసకబారడం", "Sun protection": "సూర్య రక్షణ", "Flakiness": "పొరలుగా ఊడటం", "Barrier weakness": "బారియర్ బలహీనత", "Fine lines": "సన్నని గీతలు", "Excess sebum": "అధిక సెబమ్", "Clogged pores": "మూసుకుపోయిన రంధ్రాలు", "Acne risk": "మొటిమల ప్రమాదం", "T-zone shine": "టి-జోన్ మెరుపు", "Cheek dryness": "చెంపల పొడితనం", "Uneven texture": "అసమాన నిర్మాణం", "Redness": "ఎర్రదనం", "Irritation": "చికాకు", "Barrier stress": "బారియర్ ఒత్తిడి",
    "Even and resilient": "సమంగా మరియు బలంగా", "Tight or flaky": "బిగుసుకున్న లేదా పొరలుగా", "Shiny with visible pores": "కనిపించే రంధ్రాలతో మెరుస్తుంది", "Oily center with drier cheeks": "మధ్యభాగం నూనెగా, చెంపలు పొడిగా", "Reactive or redness prone": "ప్రతిస్పందన లేదా ఎర్రదనానికి లోనయ్యే", "Maintain hydration, antioxidant support, and daily sunscreen.": "తేమ, యాంటీఆక్సిడెంట్ మద్దతు మరియు రోజువారీ సన్‌స్క్రీన్ కొనసాగించండి.", "Focus on barrier repair, humectants, and richer moisturizers.": "బారియర్ రిపేర్, హ్యూమెక్టెంట్లు మరియు రిచ్ మాయిశ్చరైజర్లపై దృష్టి పెట్టండి.", "Use light hydration, niacinamide, and oil-control actives.": "తేలిక తేమ, నియాసినామైడ్ మరియు ఆయిల్ కంట్రోల్ యాక్టివ్స్ వాడండి.", "Balance oily and dry zones separately with flexible layers.": "నూనె మరియు పొడి ప్రాంతాలను వేరువేరుగా సమతుల్యం చేయండి.", "Choose calming, fragrance-free products and patch test new actives.": "శాంతింపజేసే, సువాసనలేని ఉత్పత్తులు ఎంచుకుని కొత్త యాక్టివ్స్‌కు ప్యాచ్ టెస్ట్ చేయండి.",
    "Even tone": "సమాన టోన్", "Balanced oil": "సమతుల్య నూనె", "Good moisture retention": "మంచి తేమ నిల్వ", "Tightness": "బిగుతు", "Fine texture": "సున్నిత నిర్మాణం", "Needs barrier support": "బారియర్ మద్దతు అవసరం", "Shine prone": "మెరుపు వచ్చే స్వభావం", "Congestion risk": "రంధ్రాల మూసుకుపోయే ప్రమాదం", "Benefits from niacinamide": "నియాసినామైడ్‌తో లాభం", "Mixed oil levels": "మిశ్రమ నూనె స్థాయులు", "Adaptable routine": "అనుకూలించే రొటీన్", "Redness prone": "ఎర్రదనానికి లోనయ్యే", "Barrier care needed": "బారియర్ కేర్ అవసరం", "Patch testing recommended": "ప్యాచ్ టెస్ట్ సిఫార్సు", "Balanced Oil": "సమతుల్య నూనె", "Hydration": "తేమ", "Low Sensitivity": "తక్కువ సున్నితత్వం", "Barrier": "బారియర్",
    "Single face detected": "ఒక ముఖం గుర్తించబడింది", "Multiple faces detected": "అనేక ముఖాలు గుర్తించబడ్డాయి", "No face detected": "ముఖం గుర్తించబడలేదు", "Face detection unavailable": "ముఖ గుర్తింపు అందుబాటులో లేదు", "AI recommends this for your skin profile.": "మీ చర్మ ప్రొఫైల్‌కు ఏఐ ఇది సిఫార్సు చేస్తుంది.",
    "Recommended skincare option": "సిఫార్సు చేసిన చర్మ సంరక్షణ ఎంపిక", "Supports your skin routine": "మీ చర్మ రొటీన్‌కు మద్దతు ఇస్తుంది", "Use as directed": "సూచించిన విధంగా వాడండి",
    "Face Wash": "ఫేస్ వాష్", "Moisturizer": "మాయిశ్చరైజర్", "Sunscreen": "సన్‌స్క్రీన్", "Serum": "సీరం", "Night Cream": "నైట్ క్రీమ్", "Face Mask": "ఫేస్ మాస్క్", "Toner": "టోనర్", "Lip Balm": "లిప్ బామ్", "Eye Cream": "ఐ క్రీమ్", "Cleanser": "క్లెన్సర్",
    "Simple Refreshing Face Wash": "సాధారణ రిఫ్రెషింగ్ ఫేస్ వాష్", "Vitamin C serum": "విటమిన్ C సీరం", "Light moisturizer": "తేలిక మాయిశ్చరైజర్", "Broad spectrum SPF 50": "బ్రాడ్ స్పెక్ట్రం SPF 50", "Gentle cleanser": "సున్నిత క్లెన్సర్", "Peptide serum": "పెప్టైడ్ సీరం", "Night cream": "నైట్ క్రీమ్", "Lip balm": "లిప్ బామ్", "Mild exfoliation": "తేలిక ఎక్స్‌ఫోలియేషన్", "Hydrating mask": "తేమ మాస్క్", "Scalp and pillowcase hygiene": "స్కాల్ప్ మరియు దిండు కవర్ శుభ్రత",
    "Cream cleanser": "క్రీమ్ క్లెన్సర్", "Hyaluronic acid": "హయాలురోనిక్ యాసిడ్", "Ceramide moisturizer": "సెరమైడ్ మాయిశ్చరైజర్", "Hydrating face wash": "తేమ ఫేస్ వాష్", "Squalane serum": "స్క్వాలేన్ సీరం", "Rich night cream": "రిచ్ నైట్ క్రీమ్", "Occlusive balm": "ఒక్లూజివ్ బామ్", "No harsh scrub": "కఠిన స్క్రబ్ వద్దు", "Barrier recovery night": "బారియర్ రికవరీ రాత్రి",
    "Niacinamide serum": "నియాసినామైడ్ సీరం", "Oil-free gel moisturizer": "ఆయిల్-ఫ్రీ జెల్ మాయిశ్చరైజర్", "Salicylic cleanser": "సాలిసిలిక్ క్లెన్సర్", "BHA or zinc serum": "BHA లేదా జింక్ సీరం", "Light gel cream": "తేలిక జెల్ క్రీమ్", "Spot care": "స్పాట్ కేర్", "Clay mask": "క్లే మాస్క్", "Gentle exfoliation": "సున్నిత ఎక్స్‌ఫోలియేషన్", "Non-comedogenic mask": "నాన్-కోమెడోజెనిక్ మాస్క్", "Simple Face Wash": "సింపుల్ ఫేస్ వాష్", "Vitamin C": "విటమిన్ C", "Light moisturizer on T-zone": "టి-జోన్‌పై తేలిక మాయిశ్చరైజర్", "Hydrating cream on cheeks": "చెంపలపై తేమ క్రీమ్", "Balanced cleanser": "సమతుల్య క్లెన్సర్", "Zone-based moisturizer": "జోన్ ఆధారిత మాయిశ్చరైజర్", "Eye cream": "ఐ క్రీమ్", "Clay mask only on T-zone": "క్లే మాస్క్ టి-జోన్‌పై మాత్రమే", "Hydrating mask on cheeks": "చెంపలపై తేమ మాస్క్", "Centella serum": "సెంటెల్లా సీరం", "Mineral SPF 50": "మినరల్ SPF 50", "Panthenol serum": "పాంథెనాల్ సీరం", "Soothing mask": "శాంతింపజేసే మాస్క్", "Patch test": "ప్యాచ్ టెస్ట్", "Avoid harsh exfoliation": "కఠిన ఎక్స్‌ఫోలియేషన్ నివారించండి",
    "Peptides": "పెప్టైడ్లు", "Hyaluronic Acid": "హయాలురోనిక్ యాసిడ్", "Ceramides": "సెరమైడ్లు", "Shea Butter": "షియా బట్టర్", "Squalane": "స్క్వాలేన్", "Glycerin": "గ్లిసరిన్", "Niacinamide": "నియాసినామైడ్", "Salicylic Acid": "సాలిసిలిక్ యాసిడ్", "Clay Mask": "క్లే మాస్క్", "Oil-Free Moisturizer": "ఆయిల్-ఫ్రీ మాయిశ్చరైజర్", "Green Tea": "గ్రీన్ టీ", "Lactic Acid": "లాక్టిక్ యాసిడ్", "Centella": "సెంటెల్లా", "Panthenol": "పాంథెనాల్",
    "Skipping sunscreen": "సన్‌స్క్రీన్ వదిలేయడం", "Over-exfoliation": "అధిక ఎక్స్‌ఫోలియేషన్", "Sleeping with makeup": "మేకప్‌తో నిద్రపోవడం", "Harsh cleansers": "కఠిన క్లెన్సర్లు", "Alcohol toners": "ఆల్కహాల్ టోనర్లు", "Frequent exfoliation": "తరచూ ఎక్స్‌ఫోలియేషన్", "Heavy creams": "భారీ క్రీములు", "Coconut oil": "కొబ్బరి నూనె", "Greasy sunscreen": "చిక్కటి సన్‌స్క్రీన్", "One-size heavy creams": "ఒకే రకం భారీ క్రీములు", "Strong acids all over": "అన్ని చోట్ల బలమైన యాసిడ్లు", "Skipping moisturizer": "మాయిశ్చరైజర్ వదిలేయడం", "Alcohol": "ఆల్కహాల్", "Fragrance": "సువాసన", "Strong acids": "బలమైన యాసిడ్లు", "High-strength retinol": "అధిక శక్తి రెటినాల్",
    "2-2.5L water": "2-2.5 లీటర్ల నీరు", "7-8 hours sleep": "7-8 గంటల నిద్ర", "Colorful fruits": "రంగురంగుల పండ్లు", "30 min movement": "30 నిమిషాల కదలిక", "2.5-3L water": "2.5-3 లీటర్ల నీరు", "Humidify room": "గదిలో తేమ ఉంచండి", "Omega-3 foods": "ఒమేగా-3 ఆహారం", "Gentle exercise": "సున్నిత వ్యాయామం", "2-3L water": "2-3 లీటర్ల నీరు", "Low-glycemic meals": "తక్కువ గ్లైసెమిక్ భోజనం", "Clean phone screen": "ఫోన్ స్క్రీన్ శుభ్రం చేయండి", "Regular workouts": "నియమిత వ్యాయామాలు", "Balanced diet": "సమతుల్య ఆహారం", "Sleep schedule": "నిద్ర సమయం", "Moderate exercise": "మధ్యస్థ వ్యాయామం", "Stress reduction": "ఒత్తిడి తగ్గింపు", "Simple diet": "సరళ ఆహారం", "Sleep 7-8 hours": "7-8 గంటలు నిద్రపోండి",
    "Dullness": "మసకబారడం", "Occasional dryness": "అప్పుడప్పుడు పొడితనం", "Flaking": "పొరలుగా ఊడటం", "Barrier damage": "బారియర్ నష్టం", "Blackheads": "బ్లాక్‌హెడ్స్", "Shine": "మెరుపు", "Texture": "నిర్మాణం", "T-zone oil": "టి-జోన్ నూనె", "Stinging": "చిమ్మటం", "Maintain routine": "రొటీన్ కొనసాగించండి", "Use sunscreen daily": "ప్రతిరోజూ సన్‌స్క్రీన్ వాడండి", "Do not over-layer actives": "యాక్టివ్స్‌ను ఎక్కువగా పొరలుగా వాడకండి", "Apply moisturizer on damp skin": "తడి చర్మంపై మాయిశ్చరైజర్ వేయండి", "Use lukewarm water": "గోరువెచ్చని నీరు వాడండి", "Avoid hot showers on face": "ముఖంపై వేడి నీటి షవర్ నివారించండి", "Use non-comedogenic products": "నాన్-కోమెడోజెనిక్ ఉత్పత్తులు వాడండి", "Cleanse twice daily": "రోజుకు రెండుసార్లు శుభ్రం చేయండి", "Do not strip skin aggressively": "చర్మాన్ని కఠినంగా శుభ్రం చేయకండి", "Treat zones separately": "ప్రాంతాలను వేరువేరుగా చూసుకోండి", "Use lightweight layers": "తేలిక పొరలు వాడండి", "Do not use drying products on cheeks": "చెంపలపై పొడిబార్చే ఉత్పత్తులు వాడకండి", "Patch test products": "ఉత్పత్తులకు ప్యాచ్ టెస్ట్ చేయండి", "Use fragrance-free care": "సువాసనలేని కేర్ వాడండి", "Do not mix many actives": "అనేక యాక్టివ్స్ కలపకండి",
    "Maintain hydration and protection; keep the routine simple and consistent.": "తేమ మరియు రక్షణ కొనసాగించండి; రొటీన్‌ను సరళంగా, స్థిరంగా ఉంచండి.", "Repair the moisture barrier first, then add brightening actives slowly.": "ముందుగా తేమ బారియర్‌ను బాగు చేసి, తరువాత బ్రైటెనింగ్ యాక్టివ్స్‌ను నెమ్మదిగా జోడించండి.", "Control oil while preserving hydration; stripped skin often becomes oilier.": "తేమను కాపాడుతూ నూనెను నియంత్రించండి; ఎక్కువగా పొడిబార్చిన చర్మం మరింత నూనెగా మారవచ్చు.", "Balance oily and dry zones separately instead of forcing one routine everywhere.": "అన్ని చోట్ల ఒకే రొటీన్ బలవంతం చేయకుండా నూనె మరియు పొడి ప్రాంతాలను వేరుగా సమతుల్యం చేయండి.", "Calm the barrier and introduce one new product at a time.": "బారియర్‌ను శాంతింపజేసి, ఒకసారి ఒక కొత్త ఉత్పత్తినే పరిచయం చేయండి.",
})

TRANSLATIONS["Tamil"].update({
    "Why Choose Skin Predictor": "ஸ்கின் பிரெடிக்டரை ஏன் தேர்வு செய்ய வேண்டும்", "How It Works": "இது எப்படி செயல்படுகிறது", "Features": "அம்சங்கள்", "What Users Say": "பயனர்கள் சொல்வது", "FAQ": "அடிக்கடி கேட்கப்படும் கேள்விகள்", "Privacy Policy": "தனியுரிமைக் கொள்கை", "Size": "அளவு", "Resolution": "தீர்மானம்", "Upload time": "பதிவேற்ற நேரம்", "confidence": "நம்பிக்கை", "No report available. Analyze your skin first.": "அறிக்கை இல்லை. முதலில் தோலை பகுப்பாய்வு செய்யுங்கள்.", "Skin Report": "தோல் அறிக்கை", "Routine": "நடைமுறை", "Morning": "காலை", "Night": "இரவு", "Weekly": "வாராந்திர", "Lifestyle": "வாழ்க்கை முறை", "Products": "தயாரிப்புகள்", "Model": "மாதிரி", "Sensitivity": "உணர்திறன்", "Concerns": "கவலைகள்", "Generated by": "உருவாக்கியது", "on": "அன்று", "AI Powered Skin Analysis Report": "ஏஐ இயக்கப்பட்ட தோல் பகுப்பாய்வு அறிக்கை",
    "Analyze your facial skin using Artificial Intelligence and receive personalized skincare recommendations tailored to your skin type.": "கிருத்திம நுண்ணறிவால் உங்கள் முகத் தோலை பகுப்பாய்வு செய்து, உங்கள் தோல் வகைக்கு ஏற்ற தனிப்பயன் பரிந்துரைகளைப் பெறுங்கள்.", "Local offline intelligence": "உள்ளூர் ஆஃப்லைன் நுண்ணறிவு", "Fast": "வேகம்", "Seconds to results": "சில விநாடிகளில் முடிவுகள்", "Secure": "பாதுகாப்பானது", "No cloud upload": "கிளவுட் பதிவேற்றம் இல்லை", "Private": "தனிப்பட்டது", "Your data stays local": "உங்கள் தரவு உள்ளூரிலேயே இருக்கும்", "Quick": "விரைவு", "Instant analysis": "உடனடி பகுப்பாய்வு", "Accurate": "துல்லியம்", "Dermatologist inspired": "தோல் நிபுணர் ஊக்கத்துடன்", "Dermatologist Inspired": "தோல் நிபுணர் ஊக்கத்துடன்", "Medically reviewed": "மருத்துவ ரீதியாக மதிப்பாய்வு செய்யப்பட்டது", "AI Analysis": "ஏஐ பகுப்பாய்வு", "Skin Detection": "தோல் கண்டறிதல்", "Download Report": "அறிக்கை பதிவிறக்கு", "PNG, JPEG, JPG, or camera capture": "PNG, JPEG, JPG அல்லது கேமரா பிடிப்பு", "Predict Normal, Dry, Oily, Combination, or Sensitive skin": "சாதாரண, உலர், எண்ணெய், கலப்பு அல்லது உணர்திறன் தோலை கணிக்கவும்", "Personalized skincare routine": "தனிப்பயன் தோல் பராமரிப்பு நடைமுறை", "Professional hospital-style report": "தொழில்முறை மருத்துவமனை-பாணி அறிக்கை", "View detailed metrics": "விரிவான அளவீடுகளைப் பாருங்கள்", "Ingredient and lifestyle guidance": "பொருட்கள் மற்றும் வாழ்க்கை முறை வழிகாட்டல்",
    "How accurate is the AI analysis?": "ஏஐ பகுப்பாய்வு எவ்வளவு துல்லியம்?", "Our AI model achieves 85-95% accuracy on diverse skin types.": "எங்கள் ஏஐ மாதிரி பல்வேறு தோல் வகைகளில் 85-95% துல்லியம் பெறுகிறது.", "Is my image stored or uploaded?": "என் படம் சேமிக்கப்படுமா அல்லது பதிவேற்றப்படுமா?", "No, all processing happens locally on your device.": "இல்லை, அனைத்து செயலாக்கமும் உங்கள் சாதனத்தில் உள்ளூராக நடக்கிறது.", "Do I need internet connection?": "இணைய இணைப்பு தேவைதா?", "No, the app works completely offline.": "இல்லை, பயன்பாடு முழுமையாக ஆஃப்லைனில் இயங்கும்.",
    "Low": "குறைவு", "Medium": "மிதமான", "High": "அதிகம்", "Low-Medium": "குறைவு-மிதமான", "Balanced": "சமநிலை", "Healthy": "ஆரோக்கியம்", "Mixed": "கலப்பு", "Variable": "மாறுபடும்", "T-zone high": "டி-சோன் அதிகம்", "Acne": "முகப்பரு", "Pigmentation": "நிறமாற்றம்", "Sun Damage": "சூரிய சேதம்", "Dryness": "உலர்வு", "Mild dullness": "லேசான மங்கல்", "Sun protection": "சூரிய பாதுகாப்பு", "Flakiness": "உதிர்தல்", "Barrier weakness": "தடுப்பு பலவீனம்", "Fine lines": "மெல்லிய கோடுகள்", "Excess sebum": "அதிக செபம்", "Clogged pores": "அடைந்த துளைகள்", "Acne risk": "முகப்பரு ஆபத்து", "T-zone shine": "டி-சோன் பிரகாசம்", "Cheek dryness": "கன்ன உலர்வு", "Uneven texture": "சமமற்ற அமைப்பு", "Redness": "சிவப்பு", "Irritation": "எரிச்சல்", "Barrier stress": "தடுப்பு அழுத்தம்",
    "Even and resilient": "சமமும் வலுவும்", "Tight or flaky": "இறுக்கம் அல்லது உதிர்வு", "Shiny with visible pores": "துளைகள் தெரியும் பிரகாசம்", "Oily center with drier cheeks": "மையம் எண்ணெயாக, கன்னங்கள் உலராக", "Reactive or redness prone": "எளிதில் எதிர்வினை அல்லது சிவப்பு", "Maintain hydration, antioxidant support, and daily sunscreen.": "ஈரப்பதம், ஆன்டிஆக்ஸிடென்ட் ஆதரவு மற்றும் தினசரி சன்ஸ்கிரீன் தொடரவும்.", "Focus on barrier repair, humectants, and richer moisturizers.": "தடுப்பு பழுது, ஈரப்பதம் ஈர்க்கும் பொருட்கள் மற்றும் செறிவான மாய்ஸ்சரைசர்களில் கவனம் செலுத்துங்கள்.", "Use light hydration, niacinamide, and oil-control actives.": "லேசான ஈரப்பதம், நியாசினமைடு மற்றும் எண்ணெய் கட்டுப்பாட்டு செயற்பொருட்களைப் பயன்படுத்துங்கள்.", "Balance oily and dry zones separately with flexible layers.": "எண்ணெய் மற்றும் உலர் பகுதிகளை தனித்தனியாக சமநிலைப்படுத்துங்கள்.", "Choose calming, fragrance-free products and patch test new actives.": "அமைதிப்படுத்தும், வாசனை இல்லாத தயாரிப்புகளைத் தேர்ந்தெடுத்து புதிய செயற்பொருட்களுக்கு பேட்ச் டெஸ்ட் செய்யுங்கள்.",
    "Even tone": "சமமான நிறம்", "Balanced oil": "சமநிலை எண்ணெய்", "Good moisture retention": "நல்ல ஈரப்பத தக்கவைப்பு", "Tightness": "இறுக்கம்", "Fine texture": "மென்மையான அமைப்பு", "Needs barrier support": "தடுப்பு ஆதரவு தேவை", "Shine prone": "பிரகாசம் அதிகரிக்கும் தன்மை", "Congestion risk": "துளை அடைப்பு ஆபத்து", "Benefits from niacinamide": "நியாசினமைடால் பயன்", "Mixed oil levels": "கலப்பு எண்ணெய் நிலைகள்", "Adaptable routine": "ஏற்புடைய நடைமுறை", "Redness prone": "சிவப்பு ஏற்படும் தன்மை", "Barrier care needed": "தடுப்பு பராமரிப்பு தேவை", "Patch testing recommended": "பேட்ச் டெஸ்ட் பரிந்துரை", "Balanced Oil": "சமநிலை எண்ணெய்", "Hydration": "ஈரப்பதம்", "Low Sensitivity": "குறைந்த உணர்திறன்", "Barrier": "தடுப்பு",
    "Single face detected": "ஒரு முகம் கண்டறியப்பட்டது", "Multiple faces detected": "பல முகங்கள் கண்டறியப்பட்டன", "No face detected": "முகம் கண்டறியப்படவில்லை", "Face detection unavailable": "முக கண்டறிதல் இல்லை", "AI recommends this for your skin profile.": "உங்கள் தோல் சுயவிவரத்திற்கு ஏஐ இதை பரிந்துரைக்கிறது.",
    "Recommended skincare option": "பரிந்துரைக்கப்பட்ட தோல் பராமரிப்பு தேர்வு", "Supports your skin routine": "உங்கள் தோல் நடைமுறைக்கு ஆதரவு தருகிறது", "Use as directed": "வழிமுறையின்படி பயன்படுத்தவும்",
    "Face Wash": "முகக் கழுவி", "Moisturizer": "மாய்ஸ்சரைசர்", "Sunscreen": "சன்ஸ்கிரீன்", "Serum": "சீரம்", "Night Cream": "இரவு கிரீம்", "Face Mask": "முகமூடி", "Toner": "டோனர்", "Lip Balm": "லிப் பாம்", "Eye Cream": "கண் கிரீம்", "Cleanser": "க்ளென்சர்",
    "Simple Refreshing Face Wash": "எளிய புத்துணர்வு முகக் கழுவி", "Vitamin C serum": "விடமின் C சீரம்", "Light moisturizer": "லேசான மாய்ஸ்சரைசர்", "Broad spectrum SPF 50": "பிராட் ஸ்பெக்ட்ரம் SPF 50", "Gentle cleanser": "மென்மையான க்ளென்சர்", "Peptide serum": "பெப்டைட் சீரம்", "Night cream": "இரவு கிரீம்", "Lip balm": "லிப் பாம்", "Mild exfoliation": "லேசான எக்ஸ்ஃபோலியேஷன்", "Hydrating mask": "ஈரப்பத முகமூடி", "Scalp and pillowcase hygiene": "தலைத்தோல் மற்றும் தலையணை உறை சுத்தம்",
    "Cream cleanser": "கிரீம் க்ளென்சர்", "Hyaluronic acid": "ஹயாலுரோனிக் அமிலம்", "Ceramide moisturizer": "செரமைடு மாய்ஸ்சரைசர்", "Hydrating face wash": "ஈரப்பத முகக் கழுவி", "Squalane serum": "ஸ்குவாலேன் சீரம்", "Rich night cream": "செறிவான இரவு கிரீம்", "Occlusive balm": "ஒக்ளூசிவ் பாம்", "No harsh scrub": "கடுமையான ஸ்க்ரப் வேண்டாம்", "Barrier recovery night": "தடுப்பு மீட்பு இரவு",
    "Niacinamide serum": "நியாசினமைடு சீரம்", "Oil-free gel moisturizer": "எண்ணெய் இல்லா ஜெல் மாய்ஸ்சரைசர்", "Salicylic cleanser": "சாலிசிலிக் க்ளென்சர்", "BHA or zinc serum": "BHA அல்லது சிங்க் சீரம்", "Light gel cream": "லேசான ஜெல் கிரீம்", "Spot care": "ஸ்பாட் கேர்", "Clay mask": "களிமண் முகமூடி", "Gentle exfoliation": "மென்மையான எக்ஸ்ஃபோலியேஷன்", "Non-comedogenic mask": "நான்-கோமெடோஜெனிக் முகமூடி", "Simple Face Wash": "எளிய முகக் கழுவி", "Vitamin C": "விடமின் C", "Light moisturizer on T-zone": "டி-சோனில் லேசான மாய்ஸ்சரைசர்", "Hydrating cream on cheeks": "கன்னங்களில் ஈரப்பத கிரீம்", "Balanced cleanser": "சமநிலை க்ளென்சர்", "Zone-based moisturizer": "பகுதி அடிப்படையிலான மாய்ஸ்சரைசர்", "Eye cream": "கண் கிரீம்", "Clay mask only on T-zone": "களிமண் முகமூடி டி-சோனில் மட்டும்", "Hydrating mask on cheeks": "கன்னங்களில் ஈரப்பத முகமூடி", "Centella serum": "சென்டெல்லா சீரம்", "Mineral SPF 50": "மினரல் SPF 50", "Panthenol serum": "பாந்தெனோல் சீரம்", "Soothing mask": "அமைதிப்படுத்தும் முகமூடி", "Patch test": "பேட்ச் டெஸ்ட்", "Avoid harsh exfoliation": "கடுமையான எக்ஸ்ஃபோலியேஷனை தவிர்க்கவும்",
    "Peptides": "பெப்டைடுகள்", "Hyaluronic Acid": "ஹயாலுரோனிக் அமிலம்", "Ceramides": "செரமைடுகள்", "Shea Butter": "ஷியா பட்டர்", "Squalane": "ஸ்குவாலேன்", "Glycerin": "க்ளிசரின்", "Niacinamide": "நியாசினமைடு", "Salicylic Acid": "சாலிசிலிக் அமிலம்", "Clay Mask": "களிமண் முகமூடி", "Oil-Free Moisturizer": "எண்ணெய் இல்லா மாய்ஸ்சரைசர்", "Green Tea": "கிரீன் டீ", "Lactic Acid": "லாக்டிக் அமிலம்", "Centella": "சென்டெல்லா", "Panthenol": "பாந்தெனோல்",
    "Skipping sunscreen": "சன்ஸ்கிரீன் தவிர்த்தல்", "Over-exfoliation": "அதிக எக்ஸ்ஃபோலியேஷன்", "Sleeping with makeup": "மேக்கப்புடன் தூங்குதல்", "Harsh cleansers": "கடுமையான க்ளென்சர்கள்", "Alcohol toners": "ஆல்கஹால் டோனர்கள்", "Frequent exfoliation": "அடிக்கடி எக்ஸ்ஃபோலியேஷன்", "Heavy creams": "கனமான கிரீம்கள்", "Coconut oil": "தேங்காய் எண்ணெய்", "Greasy sunscreen": "ஒட்டும் சன்ஸ்கிரீன்", "One-size heavy creams": "ஒரே மாதிரி கனமான கிரீம்கள்", "Strong acids all over": "எங்கும் வலுவான அமிலங்கள்", "Skipping moisturizer": "மாய்ஸ்சரைசர் தவிர்த்தல்", "Alcohol": "ஆல்கஹால்", "Fragrance": "வாசனை", "Strong acids": "வலுவான அமிலங்கள்", "High-strength retinol": "அதிக வலிமை ரெட்டினால்",
    "2-2.5L water": "2-2.5 லிட்டர் தண்ணீர்", "7-8 hours sleep": "7-8 மணி நேர தூக்கம்", "Colorful fruits": "வண்ணமயமான பழங்கள்", "30 min movement": "30 நிமிடம் இயக்கம்", "2.5-3L water": "2.5-3 லிட்டர் தண்ணீர்", "Humidify room": "அறையில் ஈரப்பதம் வைத்திருங்கள்", "Omega-3 foods": "ஓமேகா-3 உணவுகள்", "Gentle exercise": "மென்மையான உடற்பயிற்சி", "2-3L water": "2-3 லிட்டர் தண்ணீர்", "Low-glycemic meals": "குறைந்த கிளைசீமிக் உணவு", "Clean phone screen": "போன் திரையை சுத்தம் செய்யுங்கள்", "Regular workouts": "தொடர்ந்த உடற்பயிற்சி", "Balanced diet": "சமநிலை உணவு", "Sleep schedule": "தூக்க அட்டவணை", "Moderate exercise": "மிதமான உடற்பயிற்சி", "Stress reduction": "மனஅழுத்த குறைப்பு", "Simple diet": "எளிய உணவு", "Sleep 7-8 hours": "7-8 மணி நேரம் தூங்குங்கள்",
    "Dullness": "மங்கல்", "Occasional dryness": "சில நேர உலர்வு", "Flaking": "உதிர்வு", "Barrier damage": "தடுப்பு சேதம்", "Blackheads": "கரும்புள்ளிகள்", "Shine": "பிரகாசம்", "Texture": "அமைப்பு", "T-zone oil": "டி-சோன் எண்ணெய்", "Stinging": "குத்தல் உணர்வு", "Maintain routine": "நடைமுறையை தொடருங்கள்", "Use sunscreen daily": "தினமும் சன்ஸ்கிரீன் பயன்படுத்துங்கள்", "Do not over-layer actives": "செயற்பொருட்களை அதிகமாக அடுக்க வேண்டாம்", "Apply moisturizer on damp skin": "ஈரமான தோலில் மாய்ஸ்சரைசர் தடவுங்கள்", "Use lukewarm water": "சூடானதல்லாத வெதுவெதுப்பான நீர் பயன்படுத்துங்கள்", "Avoid hot showers on face": "முகத்தில் சூடான நீரைத் தவிர்க்கவும்", "Use non-comedogenic products": "நான்-கோமெடோஜெனிக் தயாரிப்புகளைப் பயன்படுத்துங்கள்", "Cleanse twice daily": "நாளுக்கு இருமுறை சுத்தம் செய்யுங்கள்", "Do not strip skin aggressively": "தோலை கடுமையாக உலரச்செய்ய வேண்டாம்", "Treat zones separately": "பகுதிகளை தனித்தனியாக பராமரிக்கவும்", "Use lightweight layers": "லேசான அடுக்குகள் பயன்படுத்துங்கள்", "Do not use drying products on cheeks": "கன்னங்களில் உலரச் செய்யும் தயாரிப்புகளைப் பயன்படுத்த வேண்டாம்", "Patch test products": "தயாரிப்புகளை பேட்ச் டெஸ்ட் செய்யுங்கள்", "Use fragrance-free care": "வாசனை இல்லாத பராமரிப்பு பயன்படுத்துங்கள்", "Do not mix many actives": "பல செயற்பொருட்களை கலக்க வேண்டாம்",
    "Maintain hydration and protection; keep the routine simple and consistent.": "ஈரப்பதமும் பாதுகாப்பும் தொடரட்டும்; நடைமுறை எளிமையாகவும் நிலையாகவும் இருக்கட்டும்.", "Repair the moisture barrier first, then add brightening actives slowly.": "முதலில் ஈரப்பத தடுப்பை சரிசெய்து, பின்னர் பிரகாச செயற்பொருட்களை மெதுவாக சேர்க்கவும்.", "Control oil while preserving hydration; stripped skin often becomes oilier.": "ஈரப்பதத்தை காக்கும்படி எண்ணெயை கட்டுப்படுத்துங்கள்; அதிகமாக உலர்த்தப்பட்ட தோல் மேலும் எண்ணெயாகலாம்.", "Balance oily and dry zones separately instead of forcing one routine everywhere.": "எங்கும் ஒரே நடைமுறையை திணிக்காமல் எண்ணெய் மற்றும் உலர் பகுதிகளை தனித்தனியாக சமநிலைப்படுத்துங்கள்.", "Calm the barrier and introduce one new product at a time.": "தடுப்பை அமைதிப்படுத்தி, ஒரே நேரத்தில் ஒரு புதிய தயாரிப்பை மட்டும் அறிமுகப்படுத்துங்கள்.",
})


def t(text: str) -> str:
    return TRANSLATIONS.get(st.session_state.get("language", "English"), {}).get(text, text)


def t_value(value):
    if isinstance(value, str):
        return t(value)
    if isinstance(value, list):
        return [t_value(item) for item in value]
    if isinstance(value, tuple):
        return tuple(t_value(item) for item in value)
    if isinstance(value, dict):
        return {t(key): t_value(item) for key, item in value.items()}
    return value


def init_page(title: str, current: str) -> None:
    st.session_state.setdefault("theme_mode", "Light")
    st.session_state.setdefault("language", "English")
    st.session_state.setdefault("history", [])
    st.session_state.setdefault("favorites", [])
    st.set_page_config(page_title=f"{t(title)} | {APP_NAME}", page_icon="🧴", layout="wide", initial_sidebar_state="expanded")
    inject_css(current)
    render_sidebar(current)


def html(markup: str) -> None:
    st.markdown(markup, unsafe_allow_html=True)


def inject_css(current: str = "") -> None:
    dark = st.session_state.get("theme_mode", "Light") == "Dark"
    bg = PALETTE["dark_bg"] if dark else PALETTE["bg"]
    text = "#F8FAFC" if dark else "#1E1F2E"
    card = "rgba(42,44,68,.78)" if dark else "rgba(255,255,255,.74)"
    muted = "#CBD5E1" if dark else "#667085"
    sidebar = "linear-gradient(180deg,#17182A,#2B245D 58%,#1E1F2E)"

    html(
        f"""
        <style>
        :root {{ --primary:{PALETTE['primary']}; --secondary:{PALETTE['secondary']}; --accent:{PALETTE['accent']};
          --warning:{PALETTE['warning']}; --danger:{PALETTE['danger']}; --bg:{bg}; --text:{text}; --card:{card}; --muted:{muted}; }}
        .stApp {{ background: radial-gradient(circle at 10% 10%, rgba(108,99,255,.18), transparent 28%),
          radial-gradient(circle at 90% 8%, rgba(255,126,179,.18), transparent 24%),
          radial-gradient(circle at 58% 92%, rgba(126,217,87,.14), transparent 30%), var(--bg); color:var(--text); }}
        .block-container {{ max-width:1280px; padding-top:1.25rem; padding-bottom:2.5rem; }}
        [data-testid="stSidebar"] {{ background:{sidebar}; }}
        [data-testid="stSidebarNav"] {{ display:none; }}
        [data-testid="stSidebar"] * {{ color:#F8FAFC !important; }}
        [data-testid="stSidebar"] a {{ border-radius:18px; padding:.45rem .55rem; transition:all .18s ease; }}
        [data-testid="stSidebar"] a:hover {{ background:rgba(255,255,255,.14); transform:translateX(3px); }}
        h1,h2,h3,h4,p,li,label,span {{ letter-spacing:0; }}
        .brand-logo {{ border-radius:26px; display:grid; place-items:center;
          background:linear-gradient(135deg,var(--primary),var(--secondary)); box-shadow:0 22px 46px rgba(108,99,255,.34); }}
        .sidebar-title {{ font-size:1.55rem;font-weight:900;line-height:1.1;margin-top:.55rem; }}
        .sidebar-subtitle,.muted {{ color:var(--muted); }}
        .hero {{ position:relative; overflow:hidden; border-radius:30px; min-height:330px; padding:2.2rem;
          background:linear-gradient(135deg,rgba(108,99,255,.95),rgba(255,126,179,.78),rgba(126,217,87,.42));
          box-shadow:0 28px 80px rgba(31,33,62,.20); animation:fadeIn .55s ease both; color:#fff; }}
        .hero:before,.hero:after {{ content:""; position:absolute; border-radius:999px; background:rgba(255,255,255,.26); animation:float 5s ease-in-out infinite; }}
        .hero:before {{ width:120px;height:120px;right:9%;top:12%; }} .hero:after {{ width:72px;height:72px;right:27%;bottom:14%; animation-delay:1.1s; }}
        .hero h1 {{ font-size:clamp(2.4rem,5vw,5.2rem); line-height:1; margin:.25rem 0; color:#fff; }}
        .hero p,.hero h3 {{ color:#fff; max-width:760px; }}
        .hero-art {{ min-height:300px; border-radius:30px; display:grid; place-items:center; font-size:5.8rem;
          background:linear-gradient(135deg,rgba(255,255,255,.75),rgba(255,255,255,.24)); border:1px solid rgba(255,255,255,.6);
          box-shadow:inset 0 0 80px rgba(255,255,255,.28),0 24px 58px rgba(108,99,255,.18); animation:float 4.5s ease-in-out infinite; }}
        .glass-card,.metric-card,.feature-card,.report-panel,.testimonial-card,.product-card {{ background:var(--card); border:1px solid rgba(255,255,255,.54);
          border-radius:24px; padding:1.2rem; box-shadow:0 18px 48px rgba(31,33,62,.12); backdrop-filter:blur(16px);
          transition:transform .22s ease, box-shadow .22s ease; height:100%; color:var(--text); }}
        .glass-card:hover,.metric-card:hover,.feature-card:hover,.testimonial-card:hover,.product-card:hover {{ transform:translateY(-5px); box-shadow:0 25px 70px rgba(108,99,255,.22); }}
        .metric-card {{ background:linear-gradient(135deg,rgba(255,255,255,.90),rgba(247,248,255,.62)); color:#1E1F2E; }}
        .badge {{ display:inline-flex;align-items:center;gap:.35rem;border-radius:999px;padding:.45rem .8rem;font-weight:850;color:#101121;background:#fff; }}
        .chip {{ display:inline-block;margin:.2rem .25rem .2rem 0;padding:.45rem .75rem;border-radius:999px;
          background:linear-gradient(135deg,rgba(108,99,255,.16),rgba(255,126,179,.16)); border:1px solid rgba(108,99,255,.20); color:var(--text); }}
        .upload-box {{ border:2px dashed rgba(108,99,255,.75); border-radius:28px; padding:1.3rem; background:rgba(255,255,255,.52); }}
        .progress-shell {{ height:13px; background:rgba(148,163,184,.22); border-radius:999px; overflow:hidden; }}
        .progress-fill {{ height:100%; border-radius:999px; background:linear-gradient(90deg,var(--primary),var(--secondary),var(--accent)); animation:grow .8s ease both; }}
        .section-title {{ margin-top:1.35rem;margin-bottom:.75rem; color:var(--text); }}
        .product-image {{ height:120px;border-radius:18px;display:grid;place-items:center;font-size:3rem;background:linear-gradient(135deg,rgba(108,99,255,.18),rgba(255,126,179,.24),rgba(126,217,87,.18)); }}
        .stButton>button,.stDownloadButton>button,.stLinkButton>a {{ border-radius:999px !important; border:0 !important;
          background:linear-gradient(135deg,var(--primary),var(--secondary)) !important; color:#fff !important; font-weight:850 !important;
          box-shadow:0 14px 32px rgba(108,99,255,.30); transition:.2s ease; }}
        .stButton>button:hover,.stDownloadButton>button:hover,.stLinkButton>a:hover {{ transform:translateY(-2px); box-shadow:0 22px 48px rgba(255,126,179,.32); }}
        @keyframes fadeIn {{ from {{ opacity:0; transform:translateY(12px); }} to {{ opacity:1; transform:translateY(0); }} }}
        @keyframes float {{ 0%,100% {{ transform:translateY(0); }} 50% {{ transform:translateY(-12px); }} }}
        @keyframes grow {{ from {{ width:0; }} }}
        @media (max-width:760px) {{ .hero {{ padding:1.25rem; min-height:260px; }} .hero-art {{ min-height:190px; font-size:3.7rem; }} }}
        </style>
        """,
    )


def render_sidebar(current: str) -> None:
    pages = [
        ("Home", "🏠", "pages/1_🏠_Home.py"),
        ("Skin Analysis", "📷", "pages/2_📸_Skin_Analysis.py"),
        ("Recommendations", "💄", "pages/3_🧴_Recommendations.py"),
        ("Report", "📄", "pages/4_📄_Report.py"),
        ("About", "ℹ️", "pages/5_ℹ️_About.py"),
    ]

    with st.sidebar:
        html(
            f'<div class="brand-logo" style="width:78px;height:78px;font-size:30px">🧴✨</div>'
            f'<div class="sidebar-title">{APP_NAME}</div>'
            f'<div class="sidebar-subtitle">{t("AI Powered Skin Analysis")}</div>'
        )
        for label, icon, path in pages:
            marker = "● " if label == current else ""
            st.page_link(path, label=f"{marker}{icon} {t(label)}")

        st.divider()
        st.radio(f"🌞 {t('Theme')}", ["Light", "Dark"], horizontal=True, key="theme_mode", format_func=t)
        st.selectbox(f"🌐 {t('Language')}", LANGUAGES, key="language")
        st.markdown(f"━━━━━━━━━━━━━━━  \n{t('Version')} {APP_VERSION}  \n{t('Made with')} ❤️  \n{t('Offline AI')}")
