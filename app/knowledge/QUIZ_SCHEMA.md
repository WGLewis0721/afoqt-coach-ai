# Quiz JSON schema

When the app or user asks for a machine quiz, emit a single JSON object:

```json
{
  "quiz_id": "string",
  "subtest": "verbal_analogies|arithmetic_reasoning|word_knowledge|math_knowledge|reading_comprehension|situational_judgment|physical_science|table_reading|instrument_comprehension|block_counting|aviation_information|mixed",
  "timed_seconds": 0,
  "target_pace_sec_per_item": 19,
  "items": [
    {
      "id": "VA-gen-01",
      "topic": "part-to-whole",
      "stem": "question text",
      "choices": ["A) ...", "B) ...", "C) ...", "D) ...", "E) ..."],
      "answer": "B",
      "explanation": "one short paragraph",
      "visual": null
    }
  ]
}
```

`visual` may be an ASCII diagram string for IC, BC, or TR items. Otherwise null.
Always provide five choices when the real subtest uses five; four is acceptable only if you state that.
Answer is the letter only.
