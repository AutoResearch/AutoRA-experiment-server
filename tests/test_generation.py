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
project_types = [
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
@pytest.mark.parametrize("firebase", firebase_options)
@pytest.mark.parametrize("proj_type", project_types)
@pytest.mark.filterwarnings("ignore:Dirty template changes included automatically")
def test_all(copie, theorist, experimentalist, firebase, proj_type):
    """Tests for copier generation. Tests have been moved into subfunctions because copie is a function scoped fixture.
    This allows us to run all tests related to a generation at once instead of needing to regenerate for each test

    Args:
        copie (Any): pytest fixture responsible for running copier and cleaning up generated projects
        theorist (str): additional theorist to install
        experimentalist (str): additional experimentalists to install
        firebase (bool): Bool to indicate whether or not to use firebase
        proj_type (str): type of project to generate
    """
    copier_result = copie.copy(
        extra_answers={
            "project_name": "test",
            "theorists": theorist,
            "experimentalists": experimentalist,
            "firebase": firebase,
            "project_type": proj_type,
        }
    )

    def test_generation():
        """Test that project generation happens without issues"""
        assert copier_result.exit_code == 0
        assert copier_result.exception is None
        assert copier_result.project_dir.is_dir()

    def test_requirements():
        """Test that requirements file has necessary dependencies"""

        assert (
            copier_result.project_dir
            / "experiment-server"
            / "research_hub"
            / "requirements.txt"
        ).is_file()

        with open(
            copier_result.project_dir / "experiment-server/research_hub/requirements.txt", "r"
        ) as req_file:
            reqs = req_file.read()
            reqs_list = reqs.split("\n")

            # ast.literal_eval throws a ValueError if result.answers["theorists"/"experimentalists"] returns a string of a single
            # theorist/experimentalist instead of a list of them as would be passed in if multiple are chosen
            # e.g. 'autora[theorist-bms]' vs '['autora[theorist-bms]', 'autora[theorist-bsr]']').
            # By using try/except blocks, we can avoid needing to do any sort of string manipulation to handle these minor differences
            try:
                proj_theorists = ast.literal_eval(copier_result.answers["theorists"])
            except ValueError:
                proj_theorists = [copier_result.answers["theorists"]]

            try:
                proj_experimentalists = ast.literal_eval(
                    copier_result.answers["experimentalists"]
                )
            except ValueError:
                proj_experimentalists = [copier_result.answers["experimentalists"]]

            # Check that we are not adding 'None' in the requirements if it is chosen
            if not proj_theorists or not proj_experimentalists:
                assert "None" not in reqs_list
            else:
                for single_proj_theorist in proj_theorists:
                    assert single_proj_theorist in reqs_list

                for single_proj_experimentalist in proj_experimentalists:
                    assert single_proj_experimentalist in reqs_list

    def test_package_build():
        """Test that Vite can bundle the code without errors"""
        assert copier_result.project_dir.is_dir()

        res = subprocess.run(
            "npm run build",
            shell=True,
            check=False,
            cwd=(copier_result.project_dir / "experiment"),
        )

        assert res.returncode == 0

    test_generation()
    test_requirements()
    test_package_build()
