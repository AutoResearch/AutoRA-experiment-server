import ast
import pytest
import subprocess

theorists = [
    "None",
    "autora[theorist-darts]",
    "autora[theorist-bms]",
    "autora[theorist-bsr]",
    "['autora[theorist-bms]', 'autora[theorist-bsr]']",
]
experimentalists = [
    "None",
    "autora[experimentalist-inequality]",
    "autora[experimentalist-novelty]",
    "autora[experimentalist-nearest-value]",
    "autora[experimentalist-model-disagreement]",
    "autora[experimentalist-uncertainty]",
    "autora[experimentalist-leverage]",
    "autora[experimentalist-falsification]",
    "autora[experimentalist-mixture]",
    "autora[experimentalist-prediction-filter]",
    "['autora[experimentalist-inequality]', 'autora[experimentalist-novelty]', 'autora[experimentalist-nearest-value]']",
]
firebase_options = [False, True]
project_type = [
    "Blank",
    "HTML Button",
    "Reaction Time",
    "Multi Choice Survey",
    "Multi Select Survey",
    "Save trial parameters",
    "Lexical decision",
    "Pause/Unpause",
    "Canvas Slider Response",
    "JsPsych - Stroop",
    "JsPsych - RDK",
    "SweetBean",
    "SuperExperiment",
]


@pytest.fixture(scope="session", params=theorists)
def theorist(request):
    return request.param


@pytest.fixture(scope="session", params=experimentalists)
def experimentalist(request):
    return request.param


@pytest.fixture(scope="session", params=firebase_options)
def firebase(request):
    return request.param


@pytest.fixture(scope="session", params=project_type)
def proj_type(request):
    return request.param


@pytest.fixture
def copier_result(copie, theorist, experimentalist, firebase, proj_type):
    result = copie.copy(
        extra_answers={
            "project_name": "test",
            "theorists": theorist,
            "experimentalists": experimentalist,
            "firebase": firebase,
            "project_type": proj_type,
        }
    )

    return result


@pytest.mark.filterwarnings("ignore:Dirty template changes included automatically")
def test_generation(copier_result):
    assert copier_result.exit_code == 0
    assert copier_result.exception is None
    assert copier_result.project_dir.is_dir()


# @pytest.mark.parametrize("theorist", theorists)
# @pytest.mark.parametrize("experimentalist", experimentalists)
# @pytest.mark.parametrize("firebase", firebase)
# @pytest.mark.parametrize("proj_type", project_type)
@pytest.mark.filterwarnings("ignore:Dirty template changes included automatically")
def test_requirements(copier_result):
    """Test that requirements file has necessary dependencies

    Args:
        copie (Any): pytest fixture responsible for running copier and cleaning up generated projects
        theorist (str): additional theorist to install
        experimentalist (str): additional experimentalists to install
        firebase (bool): Bool to indicate whether or not to use firebase
        proj_type (str): type of project to generate
    """
    # result = copie.copy(
    #     extra_answers={
    #         "project_name": "test",
    #         "theorists": theorist,
    #         "experimentalists": experimentalist,
    #         "firebase": firebase,
    #         "project_type": proj_type,
    #     }
    # )

    result = copier_result

    # assert result.exit_code == 0
    # assert result.exception is None
    # assert result.project_dir.is_dir()

    assert (
        result.project_dir / "experiment" / "research_hub" / "requirements.txt"
    ).is_file()

    with open(
        result.project_dir / "experiment/research_hub/requirements.txt", "r"
    ) as req_file:
        reqs = req_file.read()
        reqs_list = reqs.split("\n")

        # ast.literal_eval throws a ValueError if result.answers["theorists"/"experimentalists"] returns a string of a single
        # theorist/experimentalist instead of a list of them as would be passed in if multiple are chosen
        # e.g. 'autora[theorist-bms]' vs '['autora[theorist-bms]', 'autora[theorist-bsr]']').
        # By using try/except blocks, we can avoid needing to do any sort of string manipulation to handle these minor differences
        try:
            proj_theorists = ast.literal_eval(result.answers["theorists"])
        except ValueError:
            proj_theorists = [result.answers["theorists"]]

        try:
            proj_experimentalists = ast.literal_eval(result.answers["experimentalists"])
        except ValueError:
            proj_experimentalists = [result.answers["experimentalists"]]

        # Check that we are not adding 'None' in the requirements if it is chosen
        if not proj_theorists or not proj_experimentalists:
            assert "None" not in reqs_list
        else:
            assert isinstance(proj_theorists, list)
            assert isinstance(proj_experimentalists, list)

            for single_proj_theorist in proj_theorists:
                assert single_proj_theorist in reqs_list

            for single_proj_experimentalist in proj_experimentalists:
                assert single_proj_experimentalist in reqs_list


@pytest.mark.filterwarnings("ignore:Dirty template changes included automatically")
def test_package_build(copier_result):
    assert copier_result.project_dir.is_dir()

    res = subprocess.run(
        "npm run build",
        shell=True,
        check=False,
        cwd=(copier_result.project_dir / "experiment"),
    )

    assert res.returncode == 0


# @pytest.mark.parametrize("firebase", firebase)
# @pytest.mark.parametrize("proj_type", project_type)
# @pytest.mark.filterwarnings("ignore:Dirty template changes included automatically")
# def test_multiselect(copie, firebase, proj_type):
#     """Test project generation and requirements when selecting multiple theorists and experimentalists

#     Args:
#         copie (Any): pytest fixture responsible for running copier and cleaning up generated projects
#         firebase (bool): Bool to indicate whether or not to use firebase
#         proj_type (str): type of project to generate
#     """
#     theorists = [
#         "autora[experimentalist-inequality]",
#         "autora[experimentalist-uncertainty]",
#     ]
#     experimentalists = [
#         "autora[experimentalist-inequality]",
#         "autora[experimentalist-novelty]",
#         "autora[experimentalist-nearest-value]",
#     ]
#     result = copie.copy(
#         extra_answers={
#             "project_name": "test",
#             "theorists": str(theorists),
#             "experimentalists": str(experimentalists),
#             "firebase": firebase,
#             "project_type": proj_type,
#         }
#     )

#     assert result.exit_code == 0
#     assert result.project_dir.is_dir()

#     assert (
#         result.project_dir / "experiment" / "research_hub" / "requirements.txt"
#     ).is_file()

#     with open(
#         result.project_dir / "experiment/research_hub/requirements.txt", "r"
#     ) as req_file:
#         reqs = req_file.read()
#         reqs_list = reqs.split("\n")

#         for theorist in theorists:
#             assert (theorist in reqs_list) == (theorist != "None")

#         for experimentalist in experimentalists:
#             assert (experimentalist in reqs_list) == (experimentalist != "None")
