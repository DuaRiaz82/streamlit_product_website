import streamlit as st
import urllib.parse

try:
    from PIL import Image
except ImportError:  # pragma: no cover
    Image = None

WHATSAPP_NUMBER = "+923112519069"


def render_product_image(image_path, size=(500, 380)):
    if Image is None:
        return image_path

    img = Image.open(image_path).convert("RGB")
    return img.resize(size, Image.Resampling.LANCZOS)

st.set_page_config(
    page_title="TechCart",
    page_icon="📱",
    layout="wide",
)

st.markdown(
    """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;
            background: #f5f7fb;
            color: #101828;
        }

        .stApp {
            background: linear-gradient(180deg, #f8fbff 0%, #eef4ff 100%);
        }

        .topbar {
            background: rgba(255, 255, 255, 0.85);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(16, 24, 40, 0.08);
            border-radius: 18px;
            padding: 18px 22px;
            margin-bottom: 20px;
            box-shadow: 0 10px 30px rgba(15, 23, 42, 0.06);
        }

        .brand {
            font-size: 2rem;
            font-weight: 800;
            color: #0f172a;
            letter-spacing: -0.04em;
        }

        .brand span {
            color: #2563eb;
        }

        .tagline {
            font-size: 1rem;
            color: #475467;
            margin-top: 6px;
        }

        .hero-box {
            background: linear-gradient(135deg, #0f172a 0%, #1d4ed8 100%);
            border-radius: 24px;
            padding: 2.2rem;
            color: white;
            box-shadow: 0 20px 40px rgba(29, 78, 216, 0.2);
        }

        .hero-box h1 {
            font-size: 2.9rem;
            line-height: 1.1;
            margin-bottom: 0.7rem;
            letter-spacing: -0.05em;
        }

        .hero-box p {
            font-size: 1.05rem;
            color: rgba(255,255,255,0.85);
        }

        .stat-box {
            background: rgba(255,255,255,0.9);
            border: 1px solid rgba(15, 23, 42, 0.06);
            border-radius: 18px;
            padding: 1rem;
            text-align: center;
            box-shadow: 0 10px 20px rgba(15, 23, 42, 0.04);
        }

        .stat-box strong {
            display: block;
            font-size: 1.6rem;
            color: #111827;
        }

        .stat-box span {
            color: #475467;
            font-size: 0.9rem;
        }

        .section-title {
            font-size: 2rem;
            font-weight: 800;
            color: #0f172a;
            letter-spacing: -0.04em;
            margin-top: 1.2rem;
        }

        .feature-card, .product-card, .info-card {
            background: rgba(255,255,255,0.92);
            border: 1px solid rgba(15, 23, 42, 0.08);
            border-radius: 20px;
            padding: 1.2rem;
            box-shadow: 0 16px 30px rgba(15, 23, 42, 0.05);
            height: 100%;
        }

        .feature-card h4, .product-card h4, .info-card h4 {
            margin-top: 0.5rem;
            margin-bottom: 0.4rem;
            color: #111827;
        }

        .feature-card p, .product-card p, .info-card p {
            color: #475467;
            margin-bottom: 0;
        }

        .stRadio > div {
            justify-content: center;
            background: rgba(255,255,255,0.8);
            border: 1px solid rgba(15, 23, 42, 0.06);
            border-radius: 999px;
            padding: 0.3rem 0.6rem;
            width: fit-content;
            margin: 0 auto 1.2rem auto;
        }

        .stRadio [role="radiogroup"] > label {
            font-weight: 600;
            color: #475467;
            padding: 0.5rem 1rem;
            border-radius: 999px;
        }

        .stRadio [role="radiogroup"] > label[data-checked="true"] {
            background: #dbeafe;
            color: #1d4ed8;
        }

        .product-tag {
            display: inline-block;
            background: #dbeafe;
            color: #1d4ed8;
            padding: 0.35rem 0.7rem;
            border-radius: 999px;
            font-size: 0.78rem;
            font-weight: 700;
            margin-bottom: 0.75rem;
        }

        .price {
            font-size: 1.15rem;
            font-weight: 800;
            color: #111827;
            margin: 0.5rem 0 0.8rem;
        }

        .shop-btn {
            background: linear-gradient(135deg, #2563eb 0%, #1d4ed8 100%);
            color: white !important;
            border: none;
            border-radius: 12px;
            padding: 0.75rem 1.1rem;
            font-weight: 700;
            text-decoration: none;
            display: inline-block;
            text-align: center;
            width: 100%;
        }

        .secondary-btn {
            background: #e2e8f0;
            color: #0f172a;
            border: none;
            border-radius: 12px;
            padding: 0.75rem 1.1rem;
            font-weight: 700;
            text-decoration: none;
            display: inline-block;
            text-align: center;
            width: 100%;
        }

        .contact-box {
            background: linear-gradient(135deg, #eff6ff 0%, #f8fafc 100%);
            border: 1px solid rgba(37, 99, 235, 0.12);
            border-radius: 22px;
            padding: 1.5rem;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="topbar">
        <div class="brand"><span>Tech</span>Cart</div>
        <div class="tagline">Smart products. Simple shopping.</div>
    </div>
    """,
    unsafe_allow_html=True,
)

menu = st.radio(
    "Menu",
    ["Home", "Products", "Categories", "About", "Contact"],
    horizontal=True,
    label_visibility="collapsed",
)

if menu == "Home":
    st.markdown(
        """
        <div class="hero-box">
            <h1>Upgrade your tech life.</h1>
            <p>Discover smart gadgets and everyday essentials designed for convenience, performance, and value.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(
            """
            <div class="stat-box">
                <strong>500+</strong>
                <span>Happy shoppers</span>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with col2:
        st.markdown(
            """
            <div class="stat-box">
                <strong>4.9/5</strong>
                <span>Customer rating</span>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with col3:
        st.markdown(
            """
            <div class="stat-box">
                <strong>24/7</strong>
                <span>Support access</span>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("<div class='section-title'>Why customers choose us</div>", unsafe_allow_html=True)

    feature_col1, feature_col2, feature_col3 = st.columns(3)
    with feature_col1:
        st.markdown(
            """
            <div class="feature-card">
                <h4>✅ Quality Products</h4>
                <p>We source reliable gadgets and trusted essentials for everyday use.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with feature_col2:
        st.markdown(
            """
            <div class="feature-card">
                <h4>💰 Affordable Prices</h4>
                <p>Premium value without the premium price tag, tailored for smart buyers.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with feature_col3:
        st.markdown(
            """
            <div class="feature-card">
                <h4>⚡ Easy Ordering</h4>
                <p>Order quickly through WhatsApp and get swift assistance from our team.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("<br>", unsafe_allow_html=True)
    st.link_button("🛍️ SHOP NOW", "#products")

elif menu == "Products":
    st.markdown("<div class='section-title'>Our Featured Products</div>", unsafe_allow_html=True)
    st.write("Explore our most popular tech essentials and make your purchase in seconds.")

    products = [
        {
            "name": "Premium Earbuds",
            "tag": "Audio",
            "description": "Comfortable wireless earbuds with deep sound and all-day convenience.",
            "price": "Rs. 1500",
            "image": "earbuds.png",
            "product_name": "Earbuds",
        },
        {
            "name": "HP Laptop",
            "tag": "Computing",
            "description": "8th Generation laptop built for productivity, study, and multitasking.",
            "price": "Rs. 15000",
            "image": "laptop.png",
            "product_name": "HP Laptop",
        },
        {
            "name": "HP Mouse",
            "tag": "Accessories",
            "description": "Wireless laptop mouse designed for smooth control and effortless movement.",
            "price": "Rs. 2000",
            "image": "mouse.png",
            "product_name": "HP Mouse",
        },
    ]

    product_columns = st.columns(3)
    for idx, product in enumerate(products):
        with product_columns[idx]:
            st.image(render_product_image(product["image"]), use_container_width=True)
            st.markdown(
                f"""
                <div class="product-card">
                    <div class="product-tag">{product['tag']}</div>
                    <h4>{product['name']}</h4>
                    <p>{product['description']}</p>
                    <div class="price">{product['price']}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
            message = (
                "Hello! I am interested in ordering:\n"
                f"Product: {product['product_name']}\n"
                f"Price: {product['price']}\n"
                "Please provide more details."
            )
            whatsapp_url = f"https://wa.me/{WHATSAPP_NUMBER}?text={urllib.parse.quote(message)}"
            st.link_button("🛍️ Buy Now", whatsapp_url, use_container_width=True)

elif menu == "Categories":
    st.markdown("<div class='section-title'>Product Categories</div>", unsafe_allow_html=True)
    cat1, cat2, cat3 = st.columns(3)

    with cat1:
        st.markdown(
            """
            <div class="info-card">
                <h4>🎧 Audio</h4>
                <p>Headphones, earbuds, sound accessories, and wireless listening devices.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with cat2:
        st.markdown(
            """
            <div class="info-card">
                <h4>💻 Computing</h4>
                <p>Laptops and productivity devices built for work, study, and everyday use.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with cat3:
        st.markdown(
            """
            <div class="info-card">
                <h4>🖱️ Accessories</h4>
                <p>Mouse, adapters, and simple add-ons that improve desk productivity.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

elif menu == "About":
    st.markdown("<div class='section-title'>About TechCart</div>", unsafe_allow_html=True)

    col_text, col_info = st.columns([2, 1])
    with col_text:
        st.write(
            "TechCart is a modern tech store focused on delivering practical gadgets at affordable prices. "
            "We aim to make quality technology easy to access for students, professionals, and everyday shoppers."
        )
        st.write(
            "Our mission is simple: offer trusted products, smooth buying experiences, and helpful support "
            "for everyone looking to upgrade their digital lifestyle."
        )
    with col_info:
        st.markdown(
            """
            <div class="info-card">
                <h4>Mission</h4>
                <p>Make smart tech affordable and accessible.</p>
                <br>
                <h4>Vision</h4>
                <p>Build a reliable shopping experience for modern customers.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

elif menu == "Contact":
    st.markdown("<div class='section-title'>Contact Us</div>", unsafe_allow_html=True)

    st.markdown(
        """
        <div class="contact-box">
            <h4>Need help with an order?</h4>
            <p>Message us on WhatsApp and we’ll assist you with product details, pricing, and delivery information.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("<br>", unsafe_allow_html=True)
    contact_message = "Hello TechCart, I would like to know more about your products and pricing."
    contact_url = f"https://wa.me/{WHATSAPP_NUMBER}?text={urllib.parse.quote(contact_message)}"
    st.link_button("💬 Chat on WhatsApp", contact_url, use_container_width=True)
