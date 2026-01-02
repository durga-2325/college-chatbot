from flask import Flask, render_template, request, jsonify
from googletrans import Translator

app = Flask(__name__)
translator = Translator()


def get_response(user_input):
    user_input = user_input.lower()

    if "college name" in user_input:
        return "The college name is Government Polytechnic College, Perundurai."

    elif "courses" in user_input:
        return "Courses offered are CSE, EEE, ECE, Civil, and Mechanical Engineering."

    elif "fees" in user_input:
        return "The yearly fee is only ₹3000."

    elif "hostel" in user_input:
        return (
            "Hostel facilities are available for both boys and girls separately. "
            "Food provided includes both vegetarian and non-vegetarian. "
            "Hostel timing is from 7 AM to 10 PM."
        )

    elif (
        "home" in user_input
        or "about college" in user_input
        or "about polytechnic" in user_input
        or "college details" in user_input
    ):
        return (
            "This Polytechnic College was started in the year 2013 at Perundurai to "
            "impart technical knowledge skills to the needy pupils in and around Erode District.\n\n"
            "It was initially housed in Government Boys Higher Secondary School at Perundurai. "
            "It was moved to its present location with permanent buildings on the National Highway in the year 2015.\n\n"
            "The area of the campus is 8.23 acres. It has an aesthetic main building and additional "
            "buildings for laboratories and workshops.\n\n"
            "Separate buildings were constructed for gym, auditorium, guest house, hostel and canteen.\n\n"
            "This polytechnic stands as an academic icon in this area and produces competent "
            "diploma engineers who shape society in a better way."
        )

    elif "scholarship" in user_input:
        return (
            "Scholarships available:\n"
            "1. Puthumai Penn – ₹1000 per month\n"
            "2. Pragati Scholarship – ₹50,000 per year"
        )

    elif "activities" in user_input or "sports" in user_input:
        return "Extra curricular activities include sports and games."

    elif "functions" in user_input or "celebration" in user_input:
        return (
            "Functions celebrated are Pongal, Onam, Women's Day, Annual Day, "
            "Farewell Day, Graduation Day, Culturals Day, Freshers Day, "
            "Independence Day, and Republic Day."
        )

    elif "rules" in user_input:
        return (
            "College rules:\n"
            "Timing: 9:20 AM to 4:50 PM\n"
            "Dress Code: Uniform is mandatory\n"
            "Bike: Must have a valid license"
        )

    elif "transport" in user_input or "bus" in user_input:
        return "College bus facility is available both in the morning and evening."

    elif "hours" in user_input:
        return "College working hours are 8 periods from 9:20 AM to 4:50 PM."
    
    elif "ce staffs" in user_input or "சி இ பணியாளர்கள்" in user_input:
        return (
             "Dr. P. VENKATESWARI B.E., M.E., Ph.D – HOD (I/C)\n"
             "Dr. S. MANIKANDAN M.E., Ph.D – Lecturer\n"
             "Dr. R. S. MOHANA B.E., M.E., Ph.D – Lecturer\n"
             "Dr. S. K. NIVETHA B.E., M.E., Ph.D – Lecturer\n"
             "Dr. R. S. RAJKUMAR B.E., M.E., Ph.D – Lecturer\n"
             "B. PREETHA B.E., M.E – Lecturer"
    )

    elif "ece staffs" in user_input or "இ சி இ பணியாளர்கள்" in user_input:
        return (
             "P. KEERTHAN M.E – HOD (I/C)\n"
             "S. SANKAR B.E., MBA – Lecturer\n"
             "Dr. R. PARAMESHWARAM M.E., Ph.D – Lecturer\n"
             "M. CHITRA M.E – Lecturer\n"
             "P. AMUDHA M.E – Lecturer\n"
             "K. DEEPIKA B.E – Lecturer"
    )

    elif "eee staffs" in user_input or "இ இ இ பணியாளர்கள்" in user_input:
        return (
             "Dr. M. POONKODI M.E., M.B.A., Ph.D – Lecturer\n"
             "P. JEYALAKSHMI M.E – Lecturer\n"
             "R. RAMPRAKASH M.E – HOD (I/C)\n"
             "PREETHI G B.E., M.E – Lecturer\n"
             "Dr. S. BHUVANESWARI M.E., Ph.D – Lecturer\n"
             "D. MURALI ITI – Skilled Assistant (Electrician)"
    )

    elif "mech staffs" in user_input or "இயந்திர பணியாளர்கள்" in user_input:
        return (
             "G. GOPAL B.E – HOD (I/C)\n"
             "M. P. KARTHICK M.Tech – Lecturer\n"
             "M. S. BARATH GANITH B.E – Lecturer\n"
             "N. KAMALRAJ M.E – Lecturer\n"
             "P. BALAMANI M.E – Lecturer\n"
             "P. LAVANYA M.E – Lecturer\n"
             "Dr. C. P. GOLDIN PRISCILLA M.E., Ph.D – Lecturer\n"
             "SOWMYA M.E – Lecturer\n"
             "P. VIJAYALAKSHMI M.E – Lecturer\n"
             "MANI K DME – Foreman Instructor\n"
             "R. SAKTHIVEL – Workshop Instructor\n"
             "G. SRIDHAR – Skilled Assistant\n"
             "N. RAJAKUMAR – Skilled Assistant"
    )

    elif "civil staffs" in user_input or "சிவில் பணியாளர்கள்" in user_input:
         return (
            "T UMAMAHESWARI B.E., M.E – HOD\n"
            "V R MONIKASRI B.E., M.E – Lecturer\n"
            "T HARIPRASATH B.E., M.E – Lecturer\n"
            "R. DHENADHAYALAN M.E – Lecturer\n"
            "A PRADHEEP B.E – Skilled Assistant"
    )

    elif "english staffs" in user_input or "ஆங்கில பணியாளர்கள்" in user_input:
         return (
             "V SUBASHCHANDRU M.A., M.Phil – Lecturer\n"
             "P ISWARYA M.A., M.Phil – Lecturer\n"
             "R NIRMALA B.Ed., M.Phil – Lecturer"
    )

    elif "mathematics staffs" in user_input or "கணித பணியாளர்கள்" in user_input:
        return (
             "Karthikeyan S M.Sc – Lecturer\n"
             "Vinayakam S M.Sc – HOD (I/C)\n"
             "B DINESH M.Sc, M.Phil, B.Ed, PGDCA – Lecturer"
    )

    elif "physics staffs" in user_input or "இயற்பியல் பணியாளர்கள்" in user_input:
        return (
             "M SARAVANAN M.Sc, M.Phil – Lecturer\n"
             "K SARAVANAKUMAR M.Sc, Ph.D – Lecturer\n"
             "R SABITHA M.Sc, M.Phil, B.Ed – Lecturer"
    )

    elif "chemistry staffs" in user_input:
        return (
            "A KANDASAMY M.Sc., M.Ed – Lecturer\n"
            "T SHOBANA M.Sc., M.Phil., B.Ed – Lecturer\n"
            "Dr J VIJILA MANOMONI M.Sc., B.Ed., M.Phil., Ph.D – Lecturer"
        )

    elif "office staff" in user_input or "office staffs" in user_input:
        return (
            "GUNASEKARAN R P A – Principal\n"
            "BALASUBRAMANIAN M B.A., B.L.I.S – Bursar\n"
            "BOOMADEVI M B.A – Office Superintendent\n"
            "NAKENDRAN K MCA – Office Superintendent\n"
            "THIYAGARAJAN A M.Sc., B.Ed – Assistant\n"
            "V MUTHUKUMAR B.E – Assistant\n"
            "V PRIYADHARSHINI – Typist\n"
            "P GOMATHI B.Com – Assistant\n"
            "VALARMATHI R SSLC – Typist\n"
            "RAJA K SSLC, ITI (MMV) – Junior Assistant\n"
            "KASIRAJAN D M.A – Record Clerk\n"
            "MEGANATHAN D B.A – Office Assistant\n"
            "SIVAKUMAR B SSLC – Office Assistant"
        )

    else:
        return "Sorry, I couldn't understand your question. Please ask about college details."


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")

    # Detect language
    detected_lang = translator.detect(user_input).lang

    # Tamil → English
    if detected_lang == "ta":
        translated_input = translator.translate(user_input, src="ta", dest="en").text
    else:
        translated_input = user_input

    # Get response
    response_en = get_response(translated_input)

    # English → Tamil
    if detected_lang == "ta":
        final_response = translator.translate(response_en, src="en", dest="ta").text
    else:
        final_response = response_en

    return jsonify({"reply": final_response})


if __name__ == "__main__":
    app.run(debug=True)
