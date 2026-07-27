import gradio as gr
from groq import Groq
from app import *

with gr.Blocks() as ap:
    gr.Markdown("## Product Management System with Groq Gen AI")

    with gr.Row():
        load = gr.Button("LOAD DUMMY DATA")
        view = gr.Button("VIEW PRODUCTS")

    output_box = gr.Textbox(label="Output", lines=40)

    load.click(
        load_dummy_data,
        outputs=output_box
    )

    view.click(
        display_products,
        outputs=output_box
    )

    # ================= ADD PRODUCTS =================

    gr.Markdown("### ADD PRODUCT")

    pid = gr.Textbox(label="PRODUCT ID")
    name = gr.Textbox(label="PRODUCT NAME")
    price = gr.Textbox(label="PRODUCT PRICE")

    addb = gr.Button("ADD PRODUCT")

    addb.click(
        add_product,
        inputs=[pid, name, price],
        outputs=output_box
    )

    # ================= SEARCH PRODUCT =================

    gr.Markdown("### SEARCH PRODUCT")

    pid = gr.Textbox(label="PRODUCT ID")

    searchb = gr.Button("SEARCH PRODUCT")

    searchb.click(
        search_product,
        inputs=pid,
        outputs=output_box
    )

    # ================= UPDATE PRODUCT =================

    gr.Markdown("### UPDATE PRODUCT")

    pid = gr.Textbox(label="PRODUCT ID")
    name = gr.Textbox(label="PRODUCT NAME")
    price = gr.Textbox(label="PRODUCT PRICE")

    updateb = gr.Button("UPDATE PRODUCT")

    updateb.click(
        update_product,
        inputs=[pid, name, price],
        outputs=output_box
    )

    # ================= DELETE PRODUCT =================

    gr.Markdown("### DELETE PRODUCT")

    pid = gr.Textbox(label="PRODUCT ID")

    deleteb = gr.Button("DELETE PRODUCT")

    deleteb.click(
        delete_product,
        inputs=pid,
        outputs=output_box
    )

    # ================= AI PRODUCT =================

    gr.Markdown("### AI PRODUCT")

    query = gr.Textbox(label="ASK AI")

    aib = gr.Button("ASK")

    aib.click(
        ai_product_details,
        inputs=query,
        outputs=output_box
    )

ap.launch()