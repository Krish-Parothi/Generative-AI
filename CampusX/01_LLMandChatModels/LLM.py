from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq()
completion = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
      {
        "role": "user",
        "content": "What is the National Dish of India?"
      }
    ],
    temperature=1,
    max_completion_tokens=8192,
    top_p=1,
    reasoning_effort="medium",
    stream=True,
    stop=None
)

for chunk in completion:
    print(chunk.choices[0].delta.content or "", end="")

    # LLM Takes Strings as input and gives back output as a String.

# OUTPUT:      India does not have an **officially declared national dish**. Because the country’s cuisine is incredibly diverse—varying by region, culture, religion, and climate—no single recipe has been designated by the government as “the” national dish.

# That said, a few dishes are often mentioned in media and popular discourse as strong contenders for an informal “national” status:

# | Dish | Why it’s often cited |
# |------|----------------------|
# | **Biryani** (especially Hyderabadi or Lucknowi/Awadhi) | A fragrant rice‑and‑meat (or vegetable) casserole that’s beloved across the subcontinent, celebrated for its layered flavors and festive appeal. |
# | **Masala Dosa** | A thin, crispy rice‑and‑lentil crepe filled with spiced potato, iconic of South Indian cuisine and widely served in restaurants nationwide. |     
# | **Thali** | Not a single dish but a platter that brings together a balanced assortment of curries, breads, rice, pickles, and desserts—representing the “complete meal” concept in many Indian households. |
# | **Roti/Chapati with Dal** | The everyday staple of wheat flatbread paired with lentil stew, found in homes from Punjab to Kerala. |
# | **Pulao / Pilaf** | A simple, aromatic rice dish that varies regionally and is served at both everyday meals and celebrations. |

# So, while you’ll frequently see **biryani** highlighted as a favorite “national” dish in articles and travel guides, it remains **unofficial**. India’s culinary identity is best understood as a mosaic of regional specialties rather than a single national recipe.




# Temperature decides how safe or how random the model’s answers are.

# Low temperature → safe, fixed, repeatable answers

# High temperature → varied, creative, sometimes wrong answers

# In simple terms:
# temperature controls how much risk the model takes while choosing words.