# Project Template Setup

This project template helps configure and scaffold your experiment web applications with various customizable options. After answering a few prompts, the template will automatically generate and set up your project according to your selections.

## Prompts and Their Usage

### 1. `project_name`
- **Type**: `string`
- **Prompt**: What is your project name?
- **Description**: This will be the name of your project directory and will be used throughout the setup process.
- **Validation**: The project name cannot be empty.

### 2. `project_type`
- **Type**: `string`
- **Prompt**: Which project do you want to configure your webapp with?
- **Description**: Choose the type of experiment you wish to build. This will scaffold the necessary files and logic for the selected. experiment type.
- **Choices**:
  - Basic
  - Blank
  - JsPsych - Stroop
  - JsPsych - RDK
  - SweetBean
  - SuperExperiment
  - *HTML Button*
  - *Reaction Time*
  - *Multi Choice Survey*
  - *Multi Select Survey*
  - *Save Trial Parameters*
  - *Lexical Decision*
  - *Pause/Unpause*
  - *Canvas Slider Response*

- **Note**: Experiments labeled in *italics* require internet connection as they are pulled from [JsPsych's GitHub Repo](https://github.com/jspsych/jsPsych/tree/main/examples)

### 3. `theorists`
- **Type**: `multiselect`
- **Prompt**: Which theorists would you like to install?
- **Choices**:
  - None
  - autora[theorist-darts]
  - autora[theorist-bms]
  - autora[theorist-bsr]
- **Default**: `None`
- **Description**: Choose one or more theorists to integrate with your experiment. These are optional dependencies, allowing you to add specific theorist modules to the project. 
- **Validation**: You cannot select `None` along with other options.

### 4. `experimentalists`
- **Type**: `multiselect`
- **Prompt**: Which experimentalists would you like to install?
- **Choices**:
  - None
  - autora[experimentalist-inequality]
  - autora[experimentalist-novelty]
  - autora[experimentalist-nearest-value]
  - autora[experimentalist-model-disagreement]
  - autora[experimentalist-uncertainty]
  - autora[experimentalist-leverage]
  - autora[experimentalist-falsification]
  - autora[experimentalist-mixture]
  - autora[experimentalist-prediction-filter]
- **Default**: `None`
- **Description**: Select one or more experimentalist modules to include in your project. These are additional tools that help design and analyze experiments.
- **Validation**: Similar to the theorists, you cannot select `None` with other options.

### 5. `firebase`
- **Type**: `bool`
- **Prompt**: Would you like to set up a firebase experiment?
- **Default**: `false`
- **Description**: If `True`, this will set up the codebase to get conditions and save data to firebase. Further setup will be required for all configuration to be complete.

### 6. `docker`
- **Type**: `bool`
- **Prompt**: Would you like to use Docker for deployment?
- **Default**: `True`
- **Description**: If `True`, Docker configuration files will be included along with appropriate documentation for setup and use, making your project easy to containerize and deploy.

### 7. `actions`
- **Type**: `bool`
- **Prompt**: Would you like to set up GitHub Actions for deployment?
- **Default**: `True`
- **Description**: If `True`, GitHub Actions configuration files will be set up for deployment to servers and to automate CI/CD for your project. Appropriate documentation will also be generated.

## Post-Generation Setup

After generating the project, the following tasks will be automatically executed:

1. **Dynamic File Creation**: 
   - Depending on the chosen `project_type`, if needed, code will be scraped from [JsPsych's GitHub Repo](https://github.com/jspsych/jsPsych/tree/main/examples) and saved locally.
   
2. **File Cleanup**:
   - The template's hook files will be removed post-setup for a clean project structure.

3. **Frontend Setup**:
   - The `experiment-ui` directory will have dependencies installed via `npm`, and a linter will be run to ensure code quality.

## Additional Notes

- Firebase setup will require additional credentials and configuration on your part. Documentation for this setup is available [here](https://autoresearch.github.io/autora/online-experiments/firebase/#firebase-project-setup)
