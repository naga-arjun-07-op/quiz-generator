<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Quiz Generator</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            padding: 20px;
            background-color: #f5f5f5;
        }

        h2 { margin-bottom: 10px; }

        .question-box, .generated-quiz {
            background: #fff;
            padding: 15px;
            border-radius: 8px;
            margin-bottom: 20px;
            box-shadow: 0 0 5px rgba(0,0,0,0.1);
        }

        .question {
            margin-bottom: 10px;
        }

        input, textarea {
            width: 100%;
            padding: 8px;
            margin-top: 5px;
        }

        button {
            padding: 10px 15px;
            background: #007bff;
            color: #fff;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }

        button:hover { background: #0056b3; }

        .options input {
            width: 95%;
            margin-bottom: 5px;
        }

    </style>
</head>
<body>

    <h2>Quiz Generator</h2>

    <div class="question-box">
        <label>Enter Question:</label>
        <textarea id="question"></textarea>

        <div class="options">
            <label>Option A:</label>
            <input type="text" id="optA">

            <label>Option B:</label>
            <input type="text" id="optB">

            <label>Option C:</label>
            <input type="text" id="optC">

            <label>Option D:</label>
            <input type="text" id="optD">
        </div>

        <label>Correct Answer (A/B/C/D):</label>
        <input type="text" id="correct">

        <button onclick="addQuestion()">Add Question</button>
    </div>

    <h3>Generated Quiz</h3>
    <div class="generated-quiz" id="quiz"></div>

    <button onclick="downloadQuiz()">Download Quiz (TXT)</button>

    <script>
        let questions = [];

        function addQuestion() {
            const q = document.getElementById("question").value; 
            const a = document.getElementById("optA").value;
            const b = document.getElementById("optB").value;
            const c = document.getElementById("optC").value;
            const d = document.getElementById("optD").value;
            const correct = document.getElementById("correct").value.toUpperCase();

            if (!q || !a || !b || !c || !d || !correct) {
                alert("Please fill all fields!");
                return;
            }

            const questionObj = {
                question: q,
                options: { A: a, B: b, C: c, D: d },
                correct: correct
            };

            questions.push(questionObj);
            displayQuiz();

            document.querySelector("textarea").value = "";
            document.querySelectorAll("input").forEach(i => i.value = "");
        }

        function displayQuiz() {
            const quizDiv = document.getElementById("quiz");
            quizDiv.innerHTML = "";

            questions.forEach((q, index) => {
                quizDiv.innerHTML += `
                    <div class="question">
                        <strong>${index + 1}. ${q.question}</strong><br>
                        A) ${q.options.A}<br>
                        B) ${q.options.B}<br>
                        C) ${q.options.C}<br>
                        D) ${q.options.D}<br>
                        <em>Correct: ${q.correct}</em>
                        <hr>
                    </div>
                `;
            });
        }

        function downloadQuiz() {
            let text = "QUIZ QUESTIONS\n\n";
            questions.forEach((q, index) => {
                text += `${index + 1}. ${q.question}\n`;
                text += `A) ${q.options.A}\n`;
                text += `B) ${q.options.B}\n`;
                text += `C) ${q.options.C}\n`;
                text += `D) ${q.options.D}\n`;
                text += `Correct: ${q.correct}\n\n`;
            });

            const blob = new Blob([text], { type: "text/plain" });
            const url = URL.createObjectURL(blob);

            const a = document.createElement("a");
            a.href = url;
            a.download = "quiz.txt";
            a.click();
        }
    </script>
</body>
</html>
