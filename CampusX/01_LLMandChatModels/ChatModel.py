from langchain_groq.chat_models import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatGroq(
    model="openai/gpt-oss-120b",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=1.9999999,
    streaming=True,
    max_tokens=1024
)

result = llm.invoke("What is the National Dish of India?")
# invoke() returns a final message, not a stream. Iterating over result is invalid.

# LangChain streams via stream() or callback handlers. Groq supports token streaming, not true character streaming. Character-level output is simulated by printing tokens with no newline and optional delay.

# print(result)
for chunk in llm.stream("What is the National Dish of India?"):
    if chunk.content:
        for ch in chunk.content:
            print(ch, end="", flush=True)

#  Output using llm.invoke : content='India does not have an officially declared “national dish” by the government. However, several foods are popularly cited as representing the country’s culinary identity:\n\n| Food often mentioned | Why it’s associated with India |\n|----------------------|--------------------------------|\n| **Biryani** | A fragrant rice dish layered with spiced meat (or vegetables), cooked in a sealed pot. It’s beloved across the subcontinent, with regional variations (Hyderabadi, Lucknowi/Kashmiri, Kolkata, etc.) that showcase India’s diverse flavors. |\n| **Thali** | A complete meal served on a round platter, featuring a balanced assortment of dishes—dal, vegetables, rice or roti, pickles, chutney, and sometimes a sweet. It reflects the principle of “one plate, many tastes.” |\n| **Masala Dosa** | A thin, crispy fermented rice‑and‑lentil crepe filled with spiced potato mash, typically served with coconut chutney and sambar. It’s a staple of South Indian cuisine that has become popular nationwide. |\n| **Butter Chicken** (Murgh Makhani) | A creamy, tomato‑based chicken curry that originated in Delhi’s restaurant scene and is now a global ambassador for Indian cuisine. |\n| **Pani Puri / Golgappa** | A street‑food snack consisting of hollow, fried puri shells filled with spiced potatoes, chickpeas, tamarind water, and herbs—celebrated for its burst of flavors. |\n\n### What most people think of as “the national dish”\n- **Biryani** is the most frequently cited candidate in media articles, travel guides, and public polls. Its rich history (influenced by Persian, Mughal, and regional Indian cooking) and pan‑Indian popularity give it a strong claim.\n- **Thali** is also a strong contender because it embodies the idea of a balanced, wholesome meal that varies by region yet follows a common structure.\n\n### Bottom line\nWhile there’s no legally designated national dish, **biryani** and **thali** are the two foods most commonly regarded as representing India’s culinary heritage. If you’re looking for a single iconic dish to try, biryani is a safe bet; if you want a broader taste of Indian flavors in one sitting, a traditional thali is the way to go.' additional_kwargs={'reasoning_content': 'The user asks: "What is the National Dish of India?" The answer: India doesn\'t have an official national dish, but many consider biryani, or thali, or masala dosa, etc. Provide explanation. No disallowed content. Provide answer.'} response_metadata={'finish_reason': 'stop', 'model_name': 'openai/gpt-oss-120b', 'system_fingerprint': 'fp_e10890e4b9', 'service_tier': 'on_demand', 'model_provider': 'groq'} id='lc_run--b38284f4-464f-4966-9278-c328ebad8a24' usage_metadata={'input_tokens': 79, 'output_tokens': 548, 'total_tokens': 627}


# Output Using: llm.stream: 
# India does not have an officially declared “national dish” in the way some countries do. Because of its vast culinary diversity—spanning dozens of regions, languages, religions, and cultural traditions—no single food has been formally adopted as the nation’s emblematic plate.
# India does not have an officially declared “national dish” in the way some countries do. Because of its vast culinary diversity—spanning dozens of regions, languages, religions, and cultural traditions—no single food has been formally adopted as the nation’s emblematic plate.
#  religions, and cultural traditions—no single food has been formally adopted as the nation’s emblematic plate.


# That said, a few dishes are frequently mentioned in popular media and by many Indians as the country’s unofficial “national” favorite:
# That said, a few dishes are frequently mentioned in popular media and by many Indians as the country’s unofficial “national” favorite:

# | Dish | Why it’s often cited |
# | Dish | Why it’s often cited |
# |------|----------------------|
# | **Biryani** | A fragrant, spiced rice dish with meat (or vegetables) that exists in many regional variations (Hyderabadi, Lucknowi, Kolkata, etc.). Its pan‑Indian p| **Biryani** | A fragrant, spiced rice dish with meat (or vegetables) that exists in many regional variations (Hyderabadi, Lucknowi, Kolkata, etc.). Its pan‑Indian popularity and celebratory status make it a strong contender. |
# | **Thali** | A complete meal served on a round platter, featuring a balanced assortment of rice, roti, dal, vegetables, pickles, yogurt, and sometimes dessert. It showcases the concept of “one plate, many flavors,” reflecting India’s culinary diversity. |
# | **Masala Dosa** | A thin, crispy fermented rice‑and‑lentil crepe filled with spiced potato, originating from South India but beloved nationwide. |
# | **Dal (lentil stew)** | Lentils are a staple across the subcontinent; a simple dal with rice or roti is a daily comfort food for millions. |
# | **Roti/Chapati** | The everyday unleavened flatbread made from whole‑wheat flour, found in almost every Indian household. |

# ### Bottom line
# - **No official national dish** has been designated by the Indian government.
# - **Biryani** is perhaps the most commonly referenced candidate in media and public opinion, but many Indians would argue that the concept of a single national dish doesn’t capture the country’s rich, regional food tapestry. Instead, dishes like thali, masala dosa, dal, and roti are equally emblematic of India’s culinary identity.
