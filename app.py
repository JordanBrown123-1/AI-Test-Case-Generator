import streamlit as st

st.set_page_config(
    page_title="AI Test Case Generator",
    page_icon="🧪",
    layout="centered"
)

st.title("🧪 AI Test Case & Bug Report Generator")

st.write(
    "Generate structured software test cases, edge cases, "
    "and bug reports from application requirements."
)

st.divider()

# Feature requirements section
st.header("Test Case Generator")

feature_description = st.text_area(
    "Describe the software feature",
    placeholder=(
        "Example: A login page with email and password fields, "
        "a Remember Me checkbox, Forgot Password link, and Login button."
    ),
    height=180
)

test_type = st.multiselect(
    "Select test types",
    [
        "Functional",
        "Negative",
        "Boundary",
        "Security",
        "Usability"
    ],
    default=["Functional", "Negative"]
)

number_of_tests = st.slider(
    "Number of test cases",
    min_value=3,
    max_value=15,
    value=5
)

generate_tests = st.button(
    "Generate Test Cases",
    type="primary"
)

if generate_tests:

    if not feature_description.strip():
        st.warning(
            "Please describe a software feature before generating test cases."
        )

    elif not test_type:
        st.warning(
            "Please select at least one test type."
        )

    else:
        st.success("Requirements received successfully!")

        st.subheader("Feature Requirements")
        st.write(feature_description)

        st.subheader("Selected Test Types")

        for test in test_type:
            st.write(f"✅ {test}")

        st.info(
            f"Ready to generate {number_of_tests} test cases."
        )

st.divider()

# Bug report section
st.header("Bug Report Generator")

bug_description = st.text_area(
    "Describe the bug",
    placeholder=(
        "Example: The login page freezes after entering "
        "an incorrect password and clicking Login."
    ),
    height=150
)

generate_bug = st.button(
    "Generate Bug Report"
)

if generate_bug:

    if not bug_description.strip():
        st.warning(
            "Please describe the bug before generating a report."
        )

    else:
        st.success("Bug description received successfully!")

        st.subheader("Reported Issue")
        st.write(bug_description)
