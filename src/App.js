import React, { useState } from 'react';
import './App.css'; // Import the CSS file

function App() {
  const [step, setStep] = useState(0);
  const [answers, setAnswers] = useState([]);
  const [question, setQuestion] = useState("You are going on vacation! Where do you want to go?");
  const [choices, setChoices] = useState([
    "To the countryside!", 
    "A cozy cottage!", 
    "New York City in the summer!", 
    "A trip in the mountains while watching the snow fall!", 
    "Paris!"
  ]);
  const [result, setResult] = useState("");

  const handleAnswer = async (answer) => {
    const newAnswers = [...answers, answer];
    setAnswers(newAnswers);

    if (step < 5) {  // Ensure it matches the step count in Flask
      const response = await fetch('http://127.0.0.1:5000/quiz', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ answers: newAnswers }),
      });

      const data = await response.json();
      if (data.result) {
        setResult(data.result);
      } else {
        setQuestion(data.question);
        setChoices(data.choices);
        setStep(step + 1);
      }
    } else {
      const response = await fetch('http://127.0.0.1:5000/result', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ answers: newAnswers }),
      });

      const data = await response.json();
      setResult(data.result);
    }
  };

  return (
    <div className="quiz-container">
      {result ? (
        <h2>{result}</h2>
      ) : (
        <div>
          <h2>{question}</h2>
          <div className="choices-container">
            {choices.map((choice, index) => (
              <button key={index} onClick={() => handleAnswer(index + 1)} className="quiz-button">
                {choice}
              </button>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}

export default App;
