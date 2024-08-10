import autora_metadata from "./data/autora_meta.json" assert { type: 'json' }
import autora_in_data from "./data/autora_in.json" assert { type: 'json' }

/*
TODO:
    - test all functions
        - create sandbox where to test all functions
        - documentation for proper data format ofr autora_*.json files
        
    - check to see if we want to combine _updateDB and _updateDoc
*/


const _updateDB = async (study, key, value) => {
    const fs = require('fs');
    const autora_metadata_file = './data/autora_meta.json';
    const file = require(autora_metadata_file);

    file.study.key = value;

    fs.writeFile(autora_metadata_file, JSON.stringify(file), function writeJSON(err) {
        if (err) return console.log(err);
        console.log(JSON.stringify(file));
        console.log('writing to ' + autora_metadata_file);
    });
}

const _updateDoc = async (doc, updated_fields) => {
    return;
}

const getCondition = async (study, pId = null) => {
    for (const key in autora_metadata) {
        if (autora_metadata[study][key]['start_time'] === null) {
            const unixTime = Math.floor(Date.now() / 1000);
            await _updateDB(study, key, { 'start_time': unixTime, 'finished': false, 'pId': pId })


            const conditions = autora_in_data[key]

            return key, conditions
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
