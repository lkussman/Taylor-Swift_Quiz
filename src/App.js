import React, { useState } from 'react';

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

    if (step < 4) {
      const response = await fetch('/quiz', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ answers: newAnswers }),
      });

      const data = await response.json();
      setQuestion(data.question);
      setChoices(data.choices);
      setStep(step + 1);
    } else {
      const response = await fetch('/result', {
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
    <div>
      {result ? (
        <h2>{result}</h2>
      ) : (
        <div>
          <h2>{question}</h2>
          {choices.map((choice, index) => (
            <button key={index} onClick={() => handleAnswer(index + 1)}>
              {choice}
            </button>
          ))}
        </div>
      )}
    </div>
  );
}

export default App;
