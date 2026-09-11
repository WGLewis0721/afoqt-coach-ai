from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
APP_DIR = Path(__file__).resolve().parent
KNOWLEDGE_DIR = APP_DIR / "knowledge"
QUESTIONS_PATH = APP_DIR / "questions" / "bank.json"
WEB_DIR = ROOT / "web"
DATA_DIR = ROOT / "data"
PROGRESS_PATH = DATA_DIR / "progress.json"

OLLAMA_URL = "http://127.0.0.1:11434"
DEFAULT_MODEL = "llama3.1"

SUBTESTS = {
    "verbal_analogies": {"label": "Verbal Analogies", "code": "VA", "items": 25, "minutes": 8, "pace": 19},
    "arithmetic_reasoning": {"label": "Arithmetic Reasoning", "code": "AR", "items": 25, "minutes": 29, "pace": 70},
    "word_knowledge": {"label": "Word Knowledge", "code": "WK", "items": 25, "minutes": 5, "pace": 12},
    "math_knowledge": {"label": "Math Knowledge", "code": "MK", "items": 25, "minutes": 22, "pace": 53},
    "reading_comprehension": {"label": "Reading Comprehension", "code": "RC", "items": 25, "minutes": 24, "pace": 58},
    "situational_judgment": {"label": "Situational Judgment", "code": "SJ", "items": 16, "minutes": 35, "pace": 130},
    "physical_science": {"label": "Physical Science", "code": "PS", "items": 20, "minutes": 10, "pace": 30},
    "table_reading": {"label": "Table Reading", "code": "TR", "items": 40, "minutes": 7, "pace": 11},
    "instrument_comprehension": {"label": "Instrument Comprehension", "code": "IC", "items": 25, "minutes": 5, "pace": 12},
    "block_counting": {"label": "Block Counting", "code": "BC", "items": 30, "minutes": 5, "pace": 10},
    "aviation_information": {"label": "Aviation Information", "code": "AI", "items": 20, "minutes": 8, "pace": 24},
}

COMPOSITES = {
    "verbal": ["verbal_analogies", "word_knowledge", "reading_comprehension"],
    "quantitative": ["arithmetic_reasoning", "math_knowledge"],
    "academic": ["verbal_analogies", "arithmetic_reasoning", "word_knowledge", "math_knowledge", "reading_comprehension"],
    "pilot": ["math_knowledge", "table_reading", "instrument_comprehension", "aviation_information"],
    "cso": ["verbal_analogies", "arithmetic_reasoning", "math_knowledge", "physical_science", "table_reading", "block_counting"],
    "abm": ["verbal_analogies", "word_knowledge", "reading_comprehension", "table_reading", "instrument_comprehension", "aviation_information"],
}

TRACK_FOCUS = {
    "cyber_software": ["quantitative", "academic", "verbal"],
    "nonrated": ["verbal", "quantitative", "academic"],
    "pilot": ["pilot", "verbal", "quantitative"],
    "cso": ["cso", "verbal", "quantitative"],
    "abm": ["abm", "verbal", "quantitative"],
    "undecided": ["quantitative", "academic", "verbal"],
}

TRACK_SUBTEST_PRIORITY = {
    "cyber_software": ["math_knowledge", "arithmetic_reasoning", "word_knowledge", "verbal_analogies", "reading_comprehension", "physical_science", "situational_judgment"],
    "nonrated": ["math_knowledge", "word_knowledge", "verbal_analogies", "arithmetic_reasoning", "reading_comprehension", "situational_judgment"],
}

FLOORS = {"verbal": 15, "quantitative": 10, "academic": None, "pilot": 25, "cso": 25, "abm": 25}

COMPETITIVE = {"verbal": 55, "quantitative": 70, "academic": 65, "pilot": 70, "cso": 60, "abm": 60}

DEFAULT_TRACK = "cyber_software"

KNOWLEDGE_ROUTES = {
    "verbal_analogies": ["VERBAL.md", "OVERVIEW.md"],
    "word_knowledge": ["VERBAL.md"],
    "reading_comprehension": ["VERBAL.md"],
    "arithmetic_reasoning": ["MATH.md"],
    "math_knowledge": ["MATH.md"],
    "physical_science": ["SCIENCE.md"],
    "aviation_information": ["AVIATION.md"],
    "instrument_comprehension": ["AVIATION.md", "SPATIAL.md"],
    "table_reading": ["SPATIAL.md"],
    "block_counting": ["SPATIAL.md"],
    "situational_judgment": ["OFFICER_JUDGMENT.md"],
    "self_description": ["OFFICER_JUDGMENT.md"],
    "overview": ["OVERVIEW.md", "TEST_DAY.md"],
    "composites": ["OVERVIEW.md"],
    "math": ["MATH.md"],
    "verbal": ["VERBAL.md"],
    "aviation": ["AVIATION.md"],
    "science": ["SCIENCE.md"],
    "spatial": ["SPATIAL.md"],
    "test_day": ["TEST_DAY.md"],
    "cyber": ["CYBER_TRACK.md", "OVERVIEW.md", "MATH.md"],
    "cyber_software": ["CYBER_TRACK.md", "OVERVIEW.md", "MATH.md"],
    "software": ["CYBER_TRACK.md", "MATH.md", "VERBAL.md"],
}
