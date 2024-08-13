// TODO: remove unused imports once firebase dependency is removed

import { waitPage, endPage, errorPage } from "./pages";
import { getCondition, setObservation } from "./autora-filestore-functions"
import main from "./main"
import axios from "axios";


const index = async () => {
    if (process.env.NODE_ENV === 'development' && process.env.NODE_APP_devNoDb === 'True') {
        await main(0, 0)
        return
    }

    if (process.env.NODE_APP_useProlificId === 'True') {
        const queryString = window.location.search;
        const urlParams = new URLSearchParams(queryString);
        prolificId = urlParams.get('PROLIFIC_PID');
    }

    let prolificId = "1"
    let condition = await getCondition('autora', prolificId)
    if (condition && (prolificId !== null || process.env.NODE_APP_useProlificId === 'False')) {
        const observation = await main(condition[0], condition[1])
        console.log(JSON.stringify(observation))

        axios.post("/data", { key: JSON.parse(observation.json()) })
            .then((response) => {
                if (response.status != 200) {
                    console.warn(response.data.error);
                }
                // "links" can also be an array of objects

            })
            .catch((error) => console.log(error));

    } else {
        errorPage()
    }


    return false;
}

await index();
