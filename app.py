# ---------------------------------------------------------
# app.py — PROFESSIONAL MULTI-PAGE UNIT CONVERTER (Gradio)
# ---------------------------------------------------------

import gradio as gr

# ---------------------------------------------------------
# 1) CONVERSION FACTORS (MODULAR + EASY TO EXTEND)
# ---------------------------------------------------------

mass_factors = {
    "kilogram": 1,
    "gram": 1000,
    "milligram": 1000000,
    "pound": 2.20462,
}

length_factors = {
    "meter": 1,
    "centimeter": 100,
    "millimeter": 1000,
    "kilometer": 0.001,
    "inch": 39.3701,
    "foot": 3.28084,
}

volume_factors = {
    "liter": 1,
    "milliliter": 1000,
    "gallon": 0.264172,
}

time_factors = {
    "second": 1,
    "minute": 1 / 60,
    "hour": 1 / 3600,
}


# ---------------------------------------------------------
# 2) GENERIC + SPECIALIZED CONVERSION FUNCTIONS
# ---------------------------------------------------------

def convert(value, from_unit, to_unit, factor_dict):
    """Generic mathematical unit conversion"""
    try:
        value = float(value)
    except:
        return "❌ Enter a numeric value."

    result = value * (factor_dict[to_unit] / factor_dict[from_unit])
    return round(result, 5)


def convert_temperature(value, from_unit, to_unit):
    """Special temperature conversion logic"""
    try:
        value = float(value)
    except:
        return "❌ Enter a numeric value."

    if from_unit == to_unit:
        return value

    if from_unit == "celsius" and to_unit == "fahrenheit":
        return round((value * 9/5) + 32, 4)
    if from_unit == "fahrenheit" and to_unit == "celsius":
        return round((value - 32) * 5/9, 4)
    if from_unit == "celsius" and to_unit == "kelvin":
        return round(value + 273.15, 4)
    if from_unit == "kelvin" and to_unit == "celsius":
        return round(value - 273.15, 4)

    return "❌ Unsupported temperature conversion."


# ---------------------------------------------------------
# 3) PROFESSIONAL MULTI-PAGE GRADIO UI
# ---------------------------------------------------------

with gr.Blocks(title="Professional Unit Converter") as app:

    gr.Markdown(
        """
        # 🌐 Unit Converter Baba  
        Convert units across **Mass, Length, Temperature, Volume, Time**  
        **Built with Python + Gradio —No API & No LLM Model.**
        ---
        """
    )

    # ---------------- TAB: MASS ----------------
    with gr.Tab("⚖️ Mass"):
        gr.Markdown("### Convert mass units (kg, g, mg, pound)")
        with gr.Row():
            mass_value = gr.Textbox(label="Value")
            mass_from = gr.Dropdown(list(mass_factors.keys()), label="From")
            mass_to = gr.Dropdown(list(mass_factors.keys()), label="To")
        mass_btn = gr.Button("Convert Mass", variant="primary")
        mass_output = gr.Textbox(label="Result")
        mass_btn.click(
            lambda v, f, t: convert(v, f, t, mass_factors),
            [mass_value, mass_from, mass_to],
            mass_output,
        )

    # ---------------- TAB: LENGTH ---------------
    with gr.Tab("📏 Length"):
        gr.Markdown("### Convert length units (meter, cm, km, inch, foot)")
        with gr.Row():
            len_value = gr.Textbox(label="Value")
            len_from = gr.Dropdown(list(length_factors.keys()), label="From")
            len_to = gr.Dropdown(list(length_factors.keys()), label="To")
        len_btn = gr.Button("Convert Length", variant="primary")
        len_output = gr.Textbox(label="Result")
        len_btn.click(
            lambda v, f, t: convert(v, f, t, length_factors),
            [len_value, len_from, len_to],
            len_output,
        )

    # --------------- TAB: TEMPERATURE -----------
    with gr.Tab("🌡 Temperature"):
        gr.Markdown("### Convert temperature units (Celsius, Fahrenheit, Kelvin)")
        with gr.Row():
            temp_value = gr.Textbox(label="Value")
            temp_from = gr.Dropdown(["celsius", "fahrenheit", "kelvin"], label="From")
            temp_to = gr.Dropdown(["celsius", "fahrenheit", "kelvin"], label="To")
        temp_btn = gr.Button("Convert Temperature", variant="primary")
        temp_output = gr.Textbox(label="Result")
        temp_btn.click(
            convert_temperature,
            [temp_value, temp_from, temp_to],
            temp_output,
        )

    # ---------------- TAB: VOLUME ---------------
    with gr.Tab("🧪 Volume"):
        gr.Markdown("### Convert volume units (liter, milliliter, gallon)")
        with gr.Row():
            vol_value = gr.Textbox(label="Value")
            vol_from = gr.Dropdown(list(volume_factors.keys()), label="From")
            vol_to = gr.Dropdown(list(volume_factors.keys()), label="To")
        vol_btn = gr.Button("Convert Volume", variant="primary")
        vol_output = gr.Textbox(label="Result")
        vol_btn.click(
            lambda v, f, t: convert(v, f, t, volume_factors),
            [vol_value, vol_from, vol_to],
            vol_output,
        )

    # ---------------- TAB: TIME -----------------
    with gr.Tab("⏱ Time"):
        gr.Markdown("### Convert time units (second, minute, hour)")
        with gr.Row():
            time_value = gr.Textbox(label="Value")
            time_from = gr.Dropdown(list(time_factors.keys()), label="From")
            time_to = gr.Dropdown(list(time_factors.keys()), label="To")
        time_btn = gr.Button("Convert Time", variant="primary")
        time_output = gr.Textbox(label="Result")
        time_btn.click(
            lambda v, f, t: convert(v, f, t, time_factors),
            [time_value, time_from, time_to],
            time_output,
        )

# ---------------------------------------------------------
# 4) RUN THE APP (Required for HuggingFace Spaces)
# ---------------------------------------------------------

app.launch()
