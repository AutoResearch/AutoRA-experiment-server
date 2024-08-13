import autora_metadata from "./conditions_db/autora_meta.json";
import autora_in_data from "./conditions_db/autora_in.json";

/*
TODO:
    - test all functions
        - create sandbox where to test all functions
        - documentation for proper data format ofr autora_*.json files
        
    - check to see if we want to combine _updateDB and _updateDoc
*/


const _updateDB = async (study, key, value) => {
    // const fs = require('fs');
    // const autora_metadata_file = './data/autora_meta.json';
    // const file = require(autora_metadata_file);

    // file.study.key = value;

    // fs.writeFile(autora_metadata_file, JSON.stringify(file), function writeJSON(err) {
    // 	if (err) return console.log(err);
    // 	console.log(JSON.stringify(file));
    // 	console.log('writing to ' + autora_metadata_file);
    // });
    return;
}

const _updateDoc = async (study, key, updated_data) => {
    autora_metadata[study][key] = updated_data;

    const fs = require(fs);

    const data = JSON.stringify(updated_data);

    // writing the JSON string content to a file
    fs.writeFile("./conditions_db/autora_meta.json", data, (error) => {
        // throwing the error
        // in case of a writing problem
        if (error) {
            // logging the error
            console.error(error);

            throw error;
        }
    });

    return;
}

const getCondition = async (study, pId = null) => {
    for (let key in autora_metadata[study]) {
        if (autora_metadata[study][key]['start_time'] === null) {
            let unixTime = Math.floor(Date.now() / 1000);
            // const updated_value = { 'start_time': unixTime, 'finished': false, 'pId': pId }
            const condition_str = autora_in_data[study][key];
            let return_arr = condition_str.slice(1, -1).split(",");
            return_arr.push(unixTime.toString());

            return return_arr
        }
    }
    return false;
}

const setObservation = async (db, study, id, observation, meta = true) => {
    /**
     * Set the metadata of the id to finished and save the data to the autora observation table
     * if meta is set to false, set don't set metadata.
     */
    if (meta) {
        _updateDoc("autora_meta", { [`${id}.finished`]: true });
    }
    _updateDoc('autora_out', { [id]: observation })
}

export { getCondition, setObservation }
