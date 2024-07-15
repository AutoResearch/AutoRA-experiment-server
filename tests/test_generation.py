import pytest

theorists = [
    "None",
    "autora[theorist-darts]",
    "autora[theorist-bms]",
    "autora[theorist-bsr]",
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
]
firebase = [False, True]
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


@pytest.mark.parametrize("theorist", theorists)
@pytest.mark.parametrize("experimentalist", experimentalists)
@pytest.mark.parametrize("firebase", firebase)
@pytest.mark.parametrize("proj_type", project_type)
@pytest.mark.filterwarnings("ignore:Dirty template changes included automatically")
def test_requirements(copie, theorist, experimentalist, firebase, proj_type):
    """Test that requirements file has necessary dependencies

    Args:
        copie (Any): pytest fixture responsible for running copier and cleaning up generated projects
        theorist (str): additional theorist to install
        experimentalist (str): additional experimentalists to install
        firebase (bool): Bool to indicate whether or not to use firebase
        proj_type (str): type of project to generate
    """
    result = copie.copy(
        extra_answers={
            "project_name": "test",
            "theorists": theorist,
            "experimentalists": experimentalist,
            "firebase": firebase,
            "project_type": proj_type,
        }
    )

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_dir.is_dir()

    assert (
        result.project_dir / "experiment" / "research_hub" / "requirements.txt"
    ).is_file()

    with open(
        result.project_dir / "experiment/research_hub/requirements.txt", "r"
    ) as req_file:
        reqs = req_file.read()
        reqs_list = reqs.split("\n")

        assert (theorist in reqs_list) == (theorist != "None")
        assert (experimentalist in reqs_list) == (experimentalist != "None")


@pytest.mark.parametrize("firebase", firebase)
@pytest.mark.parametrize("proj_type", project_type)
@pytest.mark.filterwarnings("ignore:Dirty template changes included automatically")
def test_multiselect(copie, firebase, proj_type):
    """Test project generation and requirements when selecting multiple theorists and experimentalists

    Args:
        copie (Any): pytest fixture responsible for running copier and cleaning up generated projects
        firebase (bool): Bool to indicate whether or not to use firebase
        proj_type (str): type of project to generate
    """
    theorists = [
        "autora[experimentalist-inequality]",
        "autora[experimentalist-uncertainty]",
    ]
    experimentalists = [
        "autora[experimentalist-inequality]",
        "autora[experimentalist-novelty]",
        "autora[experimentalist-nearest-value]",
    ]
    result = copie.copy(
        extra_answers={
            "project_name": "test",
            "theorists": str(theorists),
            "experimentalists": str(experimentalists),
            "firebase": firebase,
            "project_type": proj_type,
        }
    )

    assert result.exit_code == 0
    assert result.project_dir.is_dir()

    assert (
        result.project_dir / "experiment" / "research_hub" / "requirements.txt"
    ).is_file()

    with open(
        result.project_dir / "experiment/research_hub/requirements.txt", "r"
    ) as req_file:
        reqs = req_file.read()
        reqs_list = reqs.split("\n")

        for theorist in theorists:
            assert (theorist in reqs_list) == (theorist != "None")

        for experimentalist in experimentalists:
            assert (experimentalist in reqs_list) == (experimentalist != "None")
