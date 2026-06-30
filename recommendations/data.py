SKIN_PROFILES = {
    "Normal": {
        "oil": "Balanced", "hydration": "Healthy", "sensitivity": "Low",
        "texture": "Even and resilient", "severity": "Low",
        "concerns": ["Mild dullness", "Sun protection"], "score": 91,
        "risks": {"Acne": "Low", "Pigmentation": "Low", "Sun Damage": "Medium", "Dryness": "Low", "Sensitivity": "Low"},
        "explanation": "Maintain hydration, antioxidant support, and daily sunscreen.",
        "characteristics": ["Even tone", "Balanced oil", "Good moisture retention"]
    },
    "Dry": {
        "oil": "Low", "hydration": "Low", "sensitivity": "Medium",
        "texture": "Tight or flaky", "severity": "Medium",
        "concerns": ["Flakiness", "Barrier weakness", "Fine lines"], "score": 74,
        "risks": {"Acne": "Low", "Pigmentation": "Medium", "Sun Damage": "Medium", "Dryness": "High", "Sensitivity": "Medium"},
        "explanation": "Focus on barrier repair, humectants, and richer moisturizers.",
        "characteristics": ["Tightness", "Fine texture", "Needs barrier support"]
    },
    "Oily": {
        "oil": "High", "hydration": "Medium", "sensitivity": "Medium",
        "texture": "Shiny with visible pores", "severity": "Medium",
        "concerns": ["Excess sebum", "Clogged pores", "Acne risk"], "score": 79,
        "risks": {"Acne": "High", "Pigmentation": "Medium", "Sun Damage": "Medium", "Dryness": "Low", "Sensitivity": "Medium"},
        "explanation": "Use light hydration, niacinamide, and oil-control actives.",
        "characteristics": ["Shine prone", "Congestion risk", "Benefits from niacinamide"]
    },
    "Combination": {
        "oil": "T-zone high", "hydration": "Mixed", "sensitivity": "Low-Medium",
        "texture": "Oily center with drier cheeks", "severity": "Medium",
        "concerns": ["T-zone shine", "Cheek dryness", "Uneven texture"], "score": 84,
        "risks": {"Acne": "Medium", "Pigmentation": "Medium", "Sun Damage": "Medium", "Dryness": "Medium", "Sensitivity": "Low"},
        "explanation": "Balance oily and dry zones separately with flexible layers.",
        "characteristics": ["Mixed oil levels", "T-zone shine", "Adaptable routine"]
    },
    "Sensitive": {
        "oil": "Variable", "hydration": "Medium", "sensitivity": "High",
        "texture": "Reactive or redness prone", "severity": "High",
        "concerns": ["Redness", "Irritation", "Barrier stress"], "score": 70,
        "risks": {"Acne": "Medium", "Pigmentation": "Medium", "Sun Damage": "High", "Dryness": "Medium", "Sensitivity": "High"},
        "explanation": "Choose calming, fragrance-free products and patch test new actives.",
        "characteristics": ["Redness prone", "Barrier care needed", "Patch testing recommended"]
    },
}

RECOMMENDATION_DATA = {
    "Normal": {
        "morning": ["Simple Refreshing Face Wash", "Vitamin C serum", "Light moisturizer", "Broad spectrum SPF 50"],
        "night": ["Gentle cleanser", "Peptide serum", "Night cream", "Lip balm"],
        "weekly": ["Mild exfoliation", "Hydrating mask", "Scalp and pillowcase hygiene"],
        "use": ["Vitamin C", "Peptides", "Hyaluronic Acid", "Ceramides"],
        "avoid": ["Skipping sunscreen", "Over-exfoliation", "Sleeping with makeup"],
        "lifestyle": ["2-2.5L water", "7-8 hours sleep", "Colorful fruits", "30 min movement"],
        "problems": ["Dullness", "Occasional dryness"],
        "dos": ["Maintain routine", "Use sunscreen daily"],
        "donts": ["Do not over-layer actives"],
        "advice": "Maintain hydration and protection; keep the routine simple and consistent."
    },
    "Dry": {
        "morning": ["Cream cleanser", "Hyaluronic acid", "Ceramide moisturizer", "SPF 30+"],
        "night": ["Hydrating face wash", "Squalane serum", "Rich night cream", "Occlusive balm"],
        "weekly": ["Hydrating mask", "No harsh scrub", "Barrier recovery night"],
        "use": ["Ceramides", "Shea Butter", "Squalane", "Glycerin"],
        "avoid": ["Harsh cleansers", "Alcohol toners", "Frequent exfoliation"],
        "lifestyle": ["2.5-3L water", "Humidify room", "Omega-3 foods", "Gentle exercise"],
        "problems": ["Flaking", "Tightness", "Barrier damage"],
        "dos": ["Apply moisturizer on damp skin", "Use lukewarm water"],
        "donts": ["Avoid hot showers on face"],
        "advice": "Repair the moisture barrier first, then add brightening actives slowly."
    },
    "Oily": {
        "morning": ["Neutrogena Oil-Free Face Wash", "Niacinamide serum", "Oil-free gel moisturizer", "Matte SPF 50"],
        "night": ["Salicylic cleanser", "BHA or zinc serum", "Light gel cream", "Spot care"],
        "weekly": ["Clay mask", "Gentle exfoliation", "Non-comedogenic mask"],
        "use": ["Niacinamide", "Salicylic Acid", "Clay Mask", "Oil-Free Moisturizer"],
        "avoid": ["Heavy creams", "Coconut oil", "Greasy sunscreen"],
        "lifestyle": ["2-3L water", "Low-glycemic meals", "Clean phone screen", "Regular workouts"],
        "problems": ["Acne", "Blackheads", "Shine"],
        "dos": ["Use non-comedogenic products", "Cleanse twice daily"],
        "donts": ["Do not strip skin aggressively"],
        "advice": "Control oil while preserving hydration; stripped skin often becomes oilier."
    },
    "Combination": {
        "morning": ["Simple Face Wash", "Vitamin C", "Light moisturizer on T-zone", "Hydrating cream on cheeks", "SPF 50"],
        "night": ["Balanced cleanser", "Niacinamide", "Zone-based moisturizer", "Eye cream"],
        "weekly": ["Clay mask only on T-zone", "Hydrating mask on cheeks", "Gentle exfoliation"],
        "use": ["Niacinamide", "Green Tea", "Hyaluronic Acid", "Lactic Acid"],
        "avoid": ["One-size heavy creams", "Strong acids all over", "Skipping moisturizer"],
        "lifestyle": ["2-2.5L water", "Balanced diet", "Sleep schedule", "Moderate exercise"],
        "problems": ["T-zone oil", "Cheek dryness", "Texture"],
        "dos": ["Treat zones separately", "Use lightweight layers"],
        "donts": ["Do not use drying products on cheeks"],
        "advice": "Balance oily and dry zones separately instead of forcing one routine everywhere."
    },
    "Sensitive": {
        "morning": ["Cetaphil Gentle Cleanser", "Centella serum", "CeraVe Moisturizing Cream", "Mineral SPF 50"],
        "night": ["Gentle cleanser", "Panthenol serum", "Avene Cicalfate", "Lip balm"],
        "weekly": ["Soothing mask", "Patch test", "Avoid harsh exfoliation"],
        "use": ["Ceramides", "Centella", "Panthenol", "Hyaluronic Acid"],
        "avoid": ["Alcohol", "Fragrance", "Strong acids", "High-strength retinol"],
        "lifestyle": ["2-3L water", "Stress reduction", "Simple diet", "Sleep 7-8 hours"],
        "problems": ["Redness", "Stinging", "Irritation"],
        "dos": ["Patch test products", "Use fragrance-free care"],
        "donts": ["Do not mix many actives"],
        "advice": "Calm the barrier and introduce one new product at a time."
    },
}

PRODUCTS = {
    "Normal": [
        ("Face Wash", "Simple Refreshing Face Wash", "Gentle daily cleanse", "Keeps skin balanced", "Morning and night"),
        ("Moisturizer", "Plum Green Tea Moisturizer", "Light hydration", "Fresh non-greasy finish", "Morning"),
        ("Sunscreen", "Minimalist SPF 50", "Daily UV defense", "Protects tone and texture", "Every morning"),
        ("Serum", "Minimalist Vitamin C", "Antioxidant glow", "Helps dullness", "Morning"),
        ("Night Cream", "Nivea Soft Cream", "Comfort hydration", "Softens overnight", "Night"),
        ("Face Mask", "Hydrating Sheet Mask", "Weekly hydration", "Boosts glow", "Weekly"),
        ("Toner", "Rose Water Toner", "Light refresh", "Preps skin", "After cleanse"),
        ("Lip Balm", "Vaseline Lip Therapy", "Lip barrier", "Prevents dryness", "As needed"),
        ("Eye Cream", "Caffeine Eye Gel", "Under-eye care", "Refreshes tired eyes", "Night"),
    ],
    "Dry": [
        ("Face Wash", "Cetaphil Gentle Skin Cleanser", "Non-stripping cleanse", "Protects barrier", "Morning"),
        ("Cleanser", "CeraVe Hydrating Cleanser", "Creamy cleanser", "Ceramide support", "Night"),
        ("Moisturizer", "CeraVe Moisturizing Cream", "Rich barrier cream", "Locks moisture", "Twice daily"),
        ("Sunscreen", "Bioderma Photoderm Creme", "Comfort SPF", "UV protection without tightness", "Morning"),
        ("Serum", "L'Oreal Hyaluronic Acid", "Humectant serum", "Pulls water into skin", "Before cream"),
        ("Night Cream", "Cetaphil DAM", "Deep repair", "Overnight comfort", "Night"),
        ("Face Mask", "Laneige Water Sleeping Mask", "Hydrating mask", "Plump look", "Weekly"),
        ("Toner", "Klairs Supple Toner", "Hydrating toner", "Preps dry skin", "After cleanse"),
        ("Lip Balm", "Aquaphor", "Occlusive repair", "Heals dry lips", "As needed"),
        ("Eye Cream", "Ceramide Eye Cream", "Barrier eye care", "Comforts dryness", "Night"),
    ],
    "Oily": [
        ("Face Wash", "Neutrogena Oil-Free Face Wash", "Oil-control cleanser", "Reduces shine", "Twice daily"),
        ("Cleanser", "Minimalist Salicylic Cleanser", "Pore cleanser", "Helps congestion", "Night"),
        ("Moisturizer", "Neutrogena Hydro Boost", "Gel hydration", "Lightweight moisture", "Morning"),
        ("Sunscreen", "Re'equil Ultra Matte Sunscreen", "Matte SPF", "Controls greasy feel", "Morning"),
        ("Serum", "The Ordinary Niacinamide", "Sebum support", "Balances oil", "Morning or night"),
        ("Night Cream", "Ponds Super Light Gel", "Light night gel", "Hydrates without heaviness", "Night"),
        ("Face Mask", "Clay Mask", "Weekly oil reset", "Absorbs excess sebum", "Weekly"),
        ("Toner", "BHA Toner", "Pore care", "Smooths texture", "2-3 nights weekly"),
        ("Lip Balm", "Lightweight SPF Lip Balm", "Lip protection", "Non-sticky", "Daytime"),
        ("Eye Cream", "Gel Eye Cream", "Light eye hydration", "No heavy residue", "Night"),
    ],
    "Combination": [
        ("Face Wash", "Simple Face Wash", "Balanced cleanse", "Works across zones", "Twice daily"),
        ("Cleanser", "Dot & Key Barrier Cleanser", "Soft cleanse", "Protects cheeks", "Night"),
        ("Moisturizer", "Ponds Super Light Gel", "Zone-friendly hydration", "Light T-zone comfort", "Morning"),
        ("Sunscreen", "Minimalist Sunscreen SPF 50", "Light UV defense", "Comfortable daily finish", "Morning"),
        ("Serum", "Garnier Vitamin C Serum", "Brightening serum", "Tone support", "Morning"),
        ("Night Cream", "Dot & Key Cica Gel", "Calming gel", "Balances zones", "Night"),
        ("Face Mask", "Multi-mask Kit", "Clay plus hydration", "Targets zones separately", "Weekly"),
        ("Toner", "Green Tea Toner", "Balancing toner", "Controls shine gently", "After cleanse"),
        ("Lip Balm", "Hyaluronic Lip Balm", "Lip hydration", "Prevents dryness", "As needed"),
        ("Eye Cream", "Light Peptide Eye Cream", "Eye care", "Light moisture", "Night"),
    ],
    "Sensitive": [
        ("Face Wash", "Cetaphil Gentle Cleanser", "Low-irritation cleanse", "Calms reactive skin", "Morning"),
        ("Cleanser", "Avene Gentle Cleanser", "Soothing cleanse", "Minimizes stinging", "Night"),
        ("Moisturizer", "CeraVe Moisturizing Cream", "Ceramide barrier cream", "Reduces dryness", "Twice daily"),
        ("Sunscreen", "La Roche Posay Anthelios SPF50", "Sensitive SPF", "High protection", "Morning"),
        ("Serum", "Centella Ampoule", "Calming serum", "Redness support", "Night"),
        ("Night Cream", "Avene Cicalfate", "Recovery cream", "Barrier repair", "Night"),
        ("Face Mask", "Soothing Oat Mask", "Calming mask", "Comforts irritation", "Weekly"),
        ("Toner", "Fragrance-Free Hydrating Toner", "Gentle hydration", "No fragrance", "After cleanse"),
        ("Lip Balm", "Cicaplast Lips", "Barrier balm", "Repairs dry lips", "As needed"),
        ("Eye Cream", "Fragrance-Free Eye Cream", "Gentle eye care", "Hydrates without sting", "Night"),
    ],
}


def routines_for(skin: str) -> dict[str, list[str]]:
    data = RECOMMENDATION_DATA.get(skin, RECOMMENDATION_DATA["Normal"])
    return {"Morning": data["morning"], "Night": data["night"], "Weekly": data["weekly"]}


def recommendation_profile(skin: str) -> dict:
    return RECOMMENDATION_DATA.get(skin, RECOMMENDATION_DATA["Normal"])


def ingredients_for(skin: str) -> list[str]:
    return recommendation_profile(skin)["use"]


def products_for(skin: str) -> list[dict]:
    return [{"category": c, "name": n, "description": d, "benefits": b, "usage": u} for c, n, d, b, u in PRODUCTS.get(skin, PRODUCTS["Normal"])]