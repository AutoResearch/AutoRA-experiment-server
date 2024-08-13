import { errorPage } from "./pages";
import { getCondition } from "./autora-filestore-functions"
import main from "./main"

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
        return observation;
    } else {
        errorPage()
    }


    return false;
}

await index();