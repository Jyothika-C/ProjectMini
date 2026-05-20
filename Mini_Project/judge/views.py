from django.shortcuts import render
from .models import Problem, Submission
from django.shortcuts import render, get_object_or_404
from .models import Problem, Submission


def home(request):

    problems = Problem.objects.all()

    return render(request, 'home.html', {
        'problems': problems
    })


def leaderboard(request):

    rankings = Submission.objects.all().order_by('-score')

    return render(request, 'leaderboard.html', {
        'rankings': rankings
    })
import subprocess
import tempfile

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Problem


def submit_solution(request, problem_id):

    problem = get_object_or_404(
        Problem,
        id=problem_id
    )

    if request.method == 'POST':

        code = request.POST.get('code')

        with tempfile.NamedTemporaryFile(
            suffix='.py',
            delete=False,
            mode='w'
        ) as file:

            file.write(code)

            filename = file.name

        result = subprocess.run(
            ['python', filename],
            input=problem.input_data,
            text=True,
            capture_output=True
        )

        output = result.stdout.strip()

        expected = problem.expected_output.strip()

        if output == expected:

            verdict = "Accepted"

        else:

            verdict = "Wrong Answer"

        return HttpResponse(f"""
            <h1>{verdict}</h1>

            <h3>Your Output:</h3>
            <pre>{output}</pre>

            <h3>Expected Output:</h3>
            <pre>{expected}</pre>
        """)

    return render(request,
                  'submit.html',
                  {'problem': problem})
    return render(request,
                  'submit.html',
                  {'problem': problem})
import subprocess
import tempfile

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse




def submit_solution(request, problem_id):

    problem = get_object_or_404(
        Problem,
        id=problem_id
    )

    return render(request,
                  'submit.html',
                  {'problem': problem})