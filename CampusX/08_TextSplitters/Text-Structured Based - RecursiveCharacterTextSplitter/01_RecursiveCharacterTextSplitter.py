# This Recursive Character Text Splittig 
# One of the Most used Text Splitting Technique.

# In this we defines Some Seperator:
# for paragraph: \n\n
# for line change: \n
# for spaces and words: " "
# for character: "" 

# Recursive Character Text Splitter works as First it makes chunks on the basis of paragraph, if paragraph ke basis pe chunks nahi ban pata hai then, vo sentences ke basis pe chunks banane ki try krega, if sentences ke basis pe bhi nahi banta hai then vo words ke basis pe chunks banata hai, if tabh nahi hota then vo character level ke basis pe chunks banata hai.

# It Tries that Midway abruptly text split na ho taaki kuch meaning rhe uss text kaa.


from langchain_text_splitters import RecursiveCharacterTextSplitter


text = """Clarity is not achieved by accumulation but by removal of excess. When inputs are unrestricted, judgment fragments and priority collapses. Attention becomes reactive instead of directed. Thought loses hierarchy and defaults to urgency. Constraints restore structure by forcing exclusion. What remains gains weight and relevance. Decisions sharpen when options narrow. Focus stops being a feeling and becomes an operating condition. Control returns through limitation. Precision replaces noise.

Order must exist before momentum can be sustained. Movement without structure amplifies inefficiency. Systems outperform willpower because they remove choice at failure points. Repetition stabilizes output across variable conditions. Process absorbs volatility that emotion cannot handle. Discipline becomes embedded rather than performed. Predictability increases leverage. Effort compounds instead of resetting. Progress becomes mechanical. Reliability replaces intensity.

Speed often disguises misunderstanding rather than resolving it. Immediate action suppresses reflection. Delay exposes faulty assumptions and weak logic. Silence interrupts compulsive response loops. Time separates signal from urgency. Patience forces reasoning to surface. Errors reveal themselves without resistance. Understanding deepens when reaction is withheld. Accuracy increases as haste is removed. Insight emerges without reinforcement.

Autonomy is constructed through internal frameworks. Dependence persists where structure is absent. External validation weakens internal calibration. Skill compounds when feedback is informational, not emotional. Independence grows as reassurance becomes unnecessary. Thinking stabilizes under pressure. Decisions hold without approval. Competence replaces permission. Authority becomes internalized. Self-sufficiency closes the loop."""


splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0

)

chunks = splitter.split_text(text)

print(len(chunks))
print(chunks)