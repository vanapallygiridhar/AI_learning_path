from langchain_google_genai import ChatGoogleGenerativeAI
from resources import RESOURCE_LINKS


def run_agent_sync(
    google_api_key: str,
    user_goal: str,
    progress_callback=None
):
    """
    Generate a personalized learning roadmap using Gemini.
    """

    try:
        if progress_callback:
            progress_callback("Initializing Gemini AI...")

        llm = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            google_api_key=google_api_key
        )

        # Find matching resources
        goal_lower = user_goal.lower()
        resource_text = ""

        for keyword, links in RESOURCE_LINKS.items():

            if keyword in goal_lower:

                resource_text = "\nRecommended Resources:\n"

                for name, url in links.items():
                    resource_text += f"- {name}: {url}\n"

                break

        if progress_callback:
            progress_callback("Generating your learning roadmap...")

        prompt = f"""
You are an expert learning coach.

Create a detailed day-wise learning roadmap.

Goal:
{user_goal}

{resource_text}

Instructions:
- Create a structured roadmap.
- Use Day 1, Day 2, Day 3 format.
- Include topic name.
- Include learning objectives.
- Include recommended learning resources.
- Include practical task/project for each day.
- Include a mini project wherever relevant.
- Keep progression logical.
- Make roadmap beginner friendly.
- Use the provided resources whenever possible.
- End with a final capstone project.

Output format:

# Learning Roadmap

Day 1

Topic:

Objectives:
- objective 1
- objective 2

Resources:
- resource 1
- resource 2

Practice Task:

Mini Project:

Day 2

Topic:

Objectives:
- objective 1
- objective 2

Resources:
- resource 1
- resource 2

Practice Task:

Mini Project:

Continue until roadmap completion.

At the end add:

# Final Capstone Project
"""

        response = llm.invoke(prompt)

        if progress_callback:
            progress_callback("Learning roadmap generated successfully!")

        return response.content

    except Exception as e:
        raise Exception(f"Error generating roadmap: {str(e)}")