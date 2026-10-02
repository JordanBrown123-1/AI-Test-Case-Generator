import streamlit as st

def generate_test_cases(feature_description, test_types, number_of_tests):
    test_cases = []

    templates = {
        "Functional": {
            "title": "Verify feature works with valid input",
            "priority": "High",
            "preconditions": "User has access to the feature.",
            "steps": [
                "Open the application.",
                "Navigate to the feature.",
                "Enter valid input.",
                "Perform the primary action."
            ],
            "expected": "The feature completes successfully and displays the expected result."
        },

        "Negative": {
            "title": "Verify feature handles invalid input",
            "priority": "High",
            "preconditions": "User has access to the feature.",
            "steps": [
                "Open the application.",
                "Navigate to the feature.",
                "Enter invalid input.",
                "Attempt to continue."
            ],
            "expected": "The application rejects the invalid input and displays an appropriate error message."
        },

        "Boundary": {
            "title": "Verify feature handles boundary values",
            "priority": "Medium",
            "preconditions": "User has access to the feature.",
            "steps": [
                "Navigate to the feature.",
                "Enter a minimum or maximum allowed value.",
                "Submit the input."
            ],
            "expected": "The application correctly handles the boundary value without unexpected behavior."
        },

        "Security": {
            "title": "Verify feature handles potentially unsafe input",
            "priority": "High",
            "preconditions": "User has access to the feature.",
            "steps": [
                "Navigate to the feature.",
                "Enter unexpected or potentially unsafe input.",
                "Submit the request."
            ],
            "expected": "The application safely rejects or sanitizes the input without exposing sensitive information."
        },

        "Usability": {
            "title": "Verify feature is clear and usable",
            "priority": "Medium",
            "preconditions": "Application is available.",
            "steps": [
                "Navigate to the feature.",
                "Review labels and instructions.",
                "Complete the normal user workflow."
            ],
            "expected": "The feature is understandable, responsive, and easy to use."
        }
    }

    for i in range(number_of_tests):
        test_type = test_types[i % len(test_types)]
        template = templates[test_type]

        test_case = {
            "id": f"TC-{i + 1:03}",
            "title": template["title"],
            "type": test_type,
            "priority": template["priority"],
            "preconditions": template["preconditions"],
            "steps": template["steps"],
            "expected": template["expected"]
        }

        test_cases.append(test_case)

    return test_cases

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

        test_cases = generate_test_cases(
            feature_description,
            test_type,
            number_of_tests
        )
        
        st.divider()
        st.header("Generated Test Cases")
        
        for test_case in test_cases:
        
            with st.expander(
                f"{test_case['id']} — {test_case['title']}"
            ):
                st.write(f"**Test Type:** {test_case['type']}")
                st.write(f"**Priority:** {test_case['priority']}")
                st.write(
                    f"**Preconditions:** {test_case['preconditions']}"
                )
        
                st.write("**Test Steps:**")
        
                for step_number, step in enumerate(
                    test_case["steps"],
                    start=1
                ):
                    st.write(f"{step_number}. {step}")
        
                st.write(
                    f"**Expected Result:** {test_case['expected']}"
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
