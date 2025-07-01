import os
import re
from django.shortcuts import render, get_object_or_404
from openai import OpenAI
from markdown import markdown
from .models import PostDraft
from .forms import GeneratePostsForm
from content_agent.models import StrategyRequest

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_posts(request):
    posts = None

    if request.method == 'POST':
        form = GeneratePostsForm(request.POST)
        if form.is_valid():
            strategy_id = form.cleaned_data['strategy_id']
            number_of_posts = form.cleaned_data['number_of_posts']
            strategy = get_object_or_404(StrategyRequest, id=strategy_id)

            # Extract titles from the strategy.result using regex or splitting
            titles = re.findall(r'\d+\.\s*(.*)', strategy.result)
            titles = titles[:number_of_posts]  # Limit to desired number of posts

            generated_posts = []

            for title in titles:
                prompt = (
                    f"Write a detailed, SEO-friendly blog post draft (~800 words) for the following title:\n"
                    f"Title: {title}\n"
                    f"Ensure the tone matches: {strategy.tone}.\n"
                    f"The post should be helpful, well-structured, and include headings."
                )

                try:
                    response = client.chat.completions.create(
                        model="gpt-4o",
                        messages=[
                            {"role": "system", "content": "You are a professional content writer AI agent."},
                            {"role": "user", "content": prompt}
                        ]
                    )
                    content_markdown = response.choices[0].message.content
                    content_html = markdown(content_markdown)

                    post = PostDraft.objects.create(
                        strategy=strategy,
                        title=title,
                        content=content_html
                    )
                    generated_posts.append(post)

                except Exception as e:
                    generated_posts.append(f"Error generating post for {title}: {str(e)}")

            posts = generated_posts

    else:
        form = GeneratePostsForm()

    return render(request, 'content_writer_agent/generate_posts.html', {
        'form': form,
        'posts': posts
    })
