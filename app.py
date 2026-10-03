import streamlit as st

def detect_feature_type(feature_description):
    text = feature_description.lower()

    if any(word in text for word in [
        "login", "log in", "sign in", "password"
    ]):
        return "login"

    if any(word in text for word in [
        "register", "registration", "sign up", "create account"
    ]):
        return "registration"

    if any(word in text for word in [
        "search", "search bar", "search box"
    ]):
        return "search"

    if any(word in text for word in [
        "checkout", "cart", "payment", "purchase"
    ]):
        return "checkout"

    if any(word in text for word in [
        "form", "submit", "contact form"
    ]):
        return "form"

    return "general"

def generate_test_cases(feature_description, test_types, number_of_tests):
    test_cases = []
    feature_type = detect_feature_type(feature_description)

    if feature_type == "login":

        login_templates = {
            "Functional": {
                "title": "Verify login with valid credentials",
                "priority": "High",
                "preconditions": "A valid user account exists.",
                "steps": [
                    "Navigate to the login page.",
                    "Enter a valid email address.",
                    "Enter the correct password.",
                    "Click the Login button."
                ],
                "expected": (
                    "The user is successfully authenticated "
                    "and redirected to the appropriate page."
                )
            },
    
            "Negative": {
                "title": "Verify login with invalid credentials",
                "priority": "High",
                "preconditions": "The login page is available.",
                "steps": [
                    "Navigate to the login page.",
                    "Enter a valid email address.",
                    "Enter an incorrect password.",
                    "Click the Login button."
                ],
                "expected": (
                    "Login is rejected and an appropriate "
                    "error message is displayed."
                )
            },
    
            "Boundary": {
                "title": "Verify login fields handle boundary input",
                "priority": "Medium",
                "preconditions": "The login page is available.",
                "steps": [
                    "Navigate to the login page.",
                    "Enter an extremely long email address.",
                    "Enter an extremely long password.",
                    "Click the Login button."
                ],
                "expected": (
                    "The application handles the input safely "
                    "without crashing or unexpected behavior."
                )
            },
    
            "Security": {
                "title": "Verify login rejects suspicious input",
                "priority": "High",
                "preconditions": "The login page is available.",
                "steps": [
                    "Navigate to the login page.",
                    "Enter unexpected characters in the email field.",
                    "Enter unexpected characters in the password field.",
                    "Click the Login button."
                ],
                "expected": (
                    "The application safely handles the input "
                    "without exposing sensitive information."
                )
            },
    
            "Usability": {
                "title": "Verify login page usability",
                "priority": "Medium",
                "preconditions": "The login page is available.",
                "steps": [
                    "Navigate to the login page.",
                    "Verify the email and password fields are clearly labeled.",
                    "Verify the Login button is visible.",
                    "Verify the Forgot Password link is accessible.",
                    "Verify the Remember Me option is understandable."
                ],
                "expected": (
                    "All login controls are clearly labeled, "
                    "accessible, and easy to understand."
                )
            }
        }
    
        templates = login_templates
    
    else:
    
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

def generate_bug_report(bug_description):
    text = bug_description.lower()

    report = {
        "id": "BUG-001",
        "title": "Application behaves unexpectedly",
        "severity": "Medium",
        "priority": "Medium",
        "environment": "Web Application",
        "description": bug_description,
        "steps": [
            "Open the application.",
            "Navigate to the affected feature.",
            "Perform the action described in the bug.",
            "Observe the application behavior."
        ],
        "expected": (
            "The application should complete the requested action "
            "without unexpected behavior."
        ),
        "actual": bug_description
    }

    # Login-related bug
    if any(word in text for word in [
        "login", "log in", "sign in", "password"
    ]):

        report["title"] = "Login functionality behaves unexpectedly"

        report["steps"] = [
            "Navigate to the login page.",
            "Enter a valid email address.",
            "Enter the password described in the issue.",
            "Click the Login button.",
            "Observe the application behavior."
        ]

        report["expected"] = (
            "The application should process the login attempt "
            "and display an appropriate result or error message."
        )

    # Detect freezing/crashing
    if any(word in text for word in [
        "freeze", "freezes", "crash", "crashes",
        "unresponsive"
    ]):

        report["severity"] = "High"
        report["priority"] = "High"

        if "login" in text or "password" in text:
            report["title"] = (
                "Login page becomes unresponsive during login attempt"
            )

        report["actual"] = (
            "The application becomes unresponsive while "
            "performing the described action."
        )

    # Detect data loss
    elif any(word in text for word in [
        "data loss", "deleted", "lost data",
        "missing data"
    ]):

        report["severity"] = "Critical"
        report["priority"] = "High"

    # Detect visual/UI issue
    elif any(word in text for word in [
        "alignment", "overlap", "color",
        "font", "button looks", "layout"
    ]):

        report["severity"] = "Low"
        report["priority"] = "Low"

    return report

def generate_edge_cases(feature_description):
    feature_type = detect_feature_type(feature_description)

    edge_cases = {
        "login": [
            "Submit the login form with both fields empty.",
            "Submit with an empty email address.",
            "Submit with an empty password.",
            "Enter an invalid email format.",
            "Enter an extremely long email address.",
            "Enter an extremely long password.",
            "Use leading or trailing spaces in the email field.",
            "Attempt multiple failed logins in a short period.",
            "Use special characters in the input fields.",
            "Attempt login after the user session has expired."
        ],

        "registration": [
            "Submit all registration fields empty.",
            "Enter an invalid email format.",
            "Use an email address that already exists.",
            "Enter mismatched password confirmation.",
            "Enter the minimum allowed password length.",
            "Enter an extremely long password.",
            "Use special characters in name fields.",
            "Submit the form multiple times rapidly."
        ],

        "search": [
            "Search with an empty query.",
            "Search using one character.",
            "Search using an extremely long query.",
            "Search using special characters.",
            "Search using only spaces.",
            "Search for an item that does not exist.",
            "Submit multiple searches rapidly."
        ],

        "checkout": [
            "Attempt checkout with an empty cart.",
            "Use an expired payment method.",
            "Enter invalid payment information.",
            "Attempt payment twice rapidly.",
            "Refresh the page during payment.",
            "Lose network connectivity during checkout.",
            "Attempt checkout when an item becomes unavailable."
        ],

        "form": [
            "Submit the form with all fields empty.",
            "Enter extremely long input.",
            "Enter special characters.",
            "Submit the form multiple times rapidly.",
            "Enter invalid data formats.",
            "Refresh the page while completing the form."
        ],

        "general": [
            "Submit empty input.",
            "Submit extremely long input.",
            "Enter special characters.",
            "Perform the action multiple times rapidly.",
            "Refresh during the operation.",
            "Lose network connectivity during the operation."
        ]
    }

    return edge_cases[feature_type]

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

        st.subheader("⚠️ Additional Edge Cases")
        
        edge_cases = generate_edge_cases(
            feature_description
        )
        
        for edge_case in edge_cases:
            st.write(f"• {edge_case}")

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

        bug_report = generate_bug_report(
            bug_description
        )

        st.success("Bug report generated successfully!")

        st.divider()

        st.header(
            f"🐛 {bug_report['id']} — {bug_report['title']}"
        )

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Severity",
                bug_report["severity"]
            )

        with col2:
            st.metric(
                "Priority",
                bug_report["priority"]
            )

        st.write(
            f"**Environment:** {bug_report['environment']}"
        )

        st.subheader("Description")

        st.write(
            bug_report["description"]
        )

        st.subheader("Steps to Reproduce")

        for step_number, step in enumerate(
            bug_report["steps"],
            start=1
        ):
            st.write(
                f"{step_number}. {step}"
            )

        st.subheader("Expected Result")

        st.write(
            bug_report["expected"]
        )

        st.subheader("Actual Result")

        st.write(
            bug_report["actual"]
        )
