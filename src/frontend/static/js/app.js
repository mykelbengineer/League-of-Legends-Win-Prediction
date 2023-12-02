// Array of champion names
const championNames = [
    '', 'Jax', 'Sona', 'Tristana', 'Varus', 'Fiora', 'Singed',
    'Tahm_Kench', 'LeBlanc', 'Thresh', 'Karma', 'Jhin', 'Rumble',
    'Udyr', 'Lee_Sin', 'Yorick', 'Ornn', 'Kayn', 'Kassadin', 'Sivir',
    'MissFortune', 'Draven', 'Yasuo', 'Kayle', 'Shaco', 'Renekton',
    'Hecarim', 'Fizz', 'KogMaw', 'Maokai', 'Lissandra', 'Jinx',
    'Urgot', 'Fiddlesticks', 'Galio', 'Pantheon', 'Talon', 'Gangplank',
    'Ezreal', 'Gnar', 'Teemo', 'Annie', 'Mordekaiser', 'Azir',
    'Kennen', 'Riven', 'ChoGath', 'Aatrox', 'Poppy', 'Taliyah',
    'Illaoi', 'Heimerdinger', 'Alistar', 'Xin_Zhao', 'Lucian',
    'Volibear', 'Sejuani', 'Nidalee', 'Garen', 'Leona', 'Zed',
    'Blitzcrank', 'Rammus', 'VelKoz', 'Caitlyn', 'Trundle', 'Kindred',
    'Quinn', 'Ekko', 'Nami', 'Swain', 'Taric', 'Syndra', 'Rakan',
    'Skarner', 'Braum', 'Veigar', 'Xerath', 'Corki', 'Nautilus',
    'Ahri', 'Jayce', 'Darius', 'Tryndamere', 'Janna', 'Elise', 'Vayne',
    'Brand', 'Graves', 'Soraka', 'Xayah', 'Karthus', 'Vladimir',
    'Zilean', 'Katarina', 'Shyvana', 'Warwick', 'Ziggs', 'Kled',
    'KhaZix', 'Olaf', 'Twisted_Fate', 'Nunu', 'Rengar', 'Bard',
    'Irelia', 'Ivern', 'Wukong', 'Ashe', 'Kalista', 'Akali', 'Vi',
    'Amumu', 'Lulu', 'Morgana', 'Nocturne', 'Diana', 'Aurelion_Sol',
    'Zyra', 'Viktor', 'Cassiopeia', 'Nasus', 'Twitch', 'Dr._Mundo',
    'Orianna', 'Evelynn', 'RekSai', 'Lux', 'Sion', 'Camille',
    'Master_Yi', 'Ryze', 'Malphite', 'Anivia', 'Shen', 'Jarvan_IV',
    'Malzahar', 'Zac', 'Gragas'
];

const champMapping = {
    'Aatrox': 'Aatrox',
    'Ahri': 'Ahri',
    'Akali': 'Akali',
    'Alistar': 'Alistar',
    'Amumu': 'Amumu',
    'Anivia': 'Anivia',
    'Annie': 'Annie',
    'Ashe': 'Ashe',
    'Aurelion_Sol':
        'Aurelion sol',
    'Azir': 'Azir',
    'Bard': 'Bard',
    'Blitzcrank': 'Blitzcrank',
    'Brand': 'Brand',
    'Braum': 'Braum',
    'Caitlyn': 'Caitlyn',
    'Camille': 'Camille',
    'Cassiopeia': 'Cassiopeia',
    'ChoGath': 'Chogath',
    'Corki': 'Corki',
    'Darius': 'Darius',
    'Diana': 'Diana',
    'Dr._Mundo': 'Drmundo',
    'Draven': 'Draven',
    'Ekko': 'Ekko',
    'Elise': 'Elise',
    'Evelynn': 'Evelynn',
    'Ezreal': 'Ezreal',
    'Fiddlesticks': 'Fiddlesticks',
    'Fiora': 'Fiora',
    'Fizz': 'Fizz',
    'Galio': 'Galio', 
    'Gangplank': 'Gangplank', 
    'Garen': 'Garen', 
    'Gnar': 'Gnar', 
    'Gragas': 'Gragas', 
    'Graves': 'Graves', 
    'Hecarim': 'Hecarim', 
    'Heimerdinger': 'Heimerdinger', 
    'Illaoi': 'Illaoi', 
    'Irelia': 'Irelia', 
    'Ivern': 'Ivern', 
    'Janna': 'Janna', 
    'Jarvan_IV': 'Jarvan IV', 
    'Jax': 'Jax', 
    'Jayce': 'Jayce', 
    'Jhin': 'Jhin', 
    'Jinx': 'Jinx', 'Kalista': 'Kalista', 'Karma': 'Karma', 'Karthus': 'Karthus', 'Kassadin': 'Kassadin', 'Katarina': 'Katarina', 'Kayle': 'Kayle', 'Kayn': 'Kayn', 'Kennen': 
    'Kennen', 'KhaZix': 'Khazix', 'Kindred': 'Kindred', 'Kled': 'Kled', 'KogMaw': 'Kogmaw', 'LeBlanc': 'LeBlanc', 'Lee_Sin': 'Lee Sin', 'Leona': 'Leona', 'Lissandra': 'Lissandra', 'Lucian': 'Lucian', 'Lulu': 'Lulu', 'Lux': 'Lux', 'Malphite': 'Malphite', 'Malzahar': 'Malzahar', 'Maokai': 'Maokai', 'Master_Yi': 'Master Yi', 'MissFortune': 'Miss Fortune', 'Mordekaiser': 'Mordekaiser', 'Morgana': 'Morgana', 'Nami': 'Nami', 'Nasus': 'Nasus', 'Nautilus': 'Nautilus', 'Nidalee': 'Nidalee', 'Nocturne': 'Nocturne', 'Nunu': 'Nunu', 'Olaf': 'Olaf', 'Orianna': 'Orianna', 'Ornn': 'Ornn', 'Pantheon': 'Pantheon', 'Poppy': 'Poppy', 'Quinn': 'Quinn', 'Rakan': 'Rakan', 'Rammus': 'Rammus', 'RekSai': 'Reksai', 'Renekton': 'Renekton', 'Rengar': 'Rengar', 'Riven': 'Riven', 'Rumble': 'Rumble', 'Ryze': 'Ryze', 'Sejuani': 'Sejuani', 'Shaco': 'Shaco', 'Shen': 'Shen', 'Shyvana': 'Shyvana', 'Singed': 'Singed', 'Sion': 'Sion', 'Sivir': 'Sivir', 'Skarner': 'Skarner', 'Sona': 'Sona', 'Soraka': 'Soraka', 'Swain': 'Swain', 'Syndra': 'Syndra', 'Tahm_Kench': 'Tahm Kench', 'Taliyah': 'Taliyah', 'Talon': 'Talon', 'Taric': 'Taric', 'Teemo': 'Teemo', 'Thresh': 'Thresh', 'Tristana': 'Tristana', 'Trundle': 'Trundle', 'Tryndamere': 'Tryndamere', 'Twisted_Fate': 'Twisted Fate', 'Twitch': 'Twitch', 'Udyr': 'Udyr', 'Urgot': 'Urgot', 'Varus': 'Varus', 'Vayne': 'Vayne', 'Veigar': 'Veigar', 'VelKoz': 'Velkoz', 'Vi': 'Vi', 'Viktor': 'Viktor', 'Vladimir': 'Vladimir', 'Volibear': 'Volibear', 'Warwick': 'Warwick', 'Wukong': 'Wukong', 'Xayah': 'Xayah', 'Xerath': 'Xerath', 'Xin_Zhao': 'Xin Zhao', 'Yasuo': 'Yasuo', 'Yorick': 'Yorick', 'Zac': 'Zac', 'Zed': 'Zed', 'Ziggs': 'Ziggs', 'Zilean': 'Zilean', 'Zyra': 'Zyra'
};

const positions = ['', 'Top', 'Jungle', 'Mid', 'Carry', 'Support'];

const getImagePath = (championName) => {
    return `/static/images/${championName}Square.webp`;
};

const maxChampions = 5;
const counter = { value: 0 };

// Counters for each side
let yourTeamCounter = { value: 0 };
let yourTeamChamps = {};
let enemyTeamCounter = { value: 0 };
let enemyTeamChamps = {};
let ownChampion = '';
// Containers on the page
const calculateWinRateButton = document.getElementById('calculateWinRate');
const resetButton = document.getElementById('reset');
const yourTeamContainer = document.getElementById('yourTeam');
const enemyTeamContainer = document.getElementById('enemyTeam');
const yourChampDropdown = document.getElementById('yourChampion');
const yourChampContainer = document.getElementById('yourChampionContainer');
const resultsConatiner = document.getElementById('results');

const updateChampionImage = (championName, champContainer, counter, lanePosition) => {
    if (counter.value < maxChampions) {
        // Create a container for both the image and the name
        const champElement = document.createElement('card');
        champElement.classList.add('card', 'align-items-center', 'champion-element');

        // Create the image element
        const champImg = document.createElement('img');
        const imagePath = getImagePath(championName);
        champImg.setAttribute('src', imagePath);
        champImg.setAttribute('alt', championName);
        champImg.setAttribute('style', "width:90%")
        champImg.classList.add('img-fluid', 'champion-thumbnail');
        champElement.appendChild(champImg);

        const champInfo = document.createElement('container');
        champInfo.setAttribute('id', 'champCard');
        champElement.appendChild(champInfo);

        // Create the name element
        const champName = document.createElement('h4');
        champName.textContent = championName;
        champName.classList.add('ms-2', 'champion-name');
        champInfo.appendChild(champName);

        // Create the name element
        const pos = document.createElement('p');
        pos.textContent = lanePosition;
        pos.classList.add('ms-2', 'lane-position');
        champInfo.appendChild(pos);

        // Create the delete button
        const deleteButton = document.createElement('button');
        deleteButton.textContent = 'X';
        deleteButton.classList.add('delete-btn');
        deleteButton.addEventListener('click', function () {
            let name = champElement.childNodes[0].alt
            if (champElement.parentElement.id === "yourTeam") {
                delete yourTeamChamps[name]
            } else if (champElement.parentElement.id === "enemyTeam") {
                delete enemyTeamChamps[name]
            }
            champElement.remove();
            counter.value--;
            updateCalculateWinRateButton();
        });

        // Append both to the container
        champElement.appendChild(champImg);
        champElement.appendChild(champName);
        champElement.appendChild(deleteButton);

        // Append or replace the champion element in the container
        if (champContainer.children[counter.value]) {
            champContainer.replaceChild(champElement, champContainer.children[counter.value]);
        } else {
            champContainer.appendChild(champElement);
        }
    }
};


const populateDropdown = (dropdownId, championImageContainerId, teamType, dropdownPositionId, button) => {
    const dropdown = document.getElementById(dropdownId);
    const dropdownPosition = document.getElementById(dropdownPositionId);
    const champContainer = document.getElementById(championImageContainerId);
    const addButton = document.getElementById(button);

    championNames.forEach(championName => {
        const option = document.createElement('option');
        option.value = championName;
        option.textContent = championName;
        dropdown.appendChild(option);
    });

    positions.forEach(lane => {
        const option = document.createElement('option');
        option.value = lane;
        option.textContent = lane;
        dropdownPosition.appendChild(option);
    });
    updateCalculateWinRateButton()
    addButton.addEventListener('click', (event) => {
        if (teamType === 'yourTeam' &&
            yourTeamCounter.value < maxChampions && // no more than 5 champs
            dropdown.value != '' && // no blank champ
            dropdownPosition.value != '' && // no blank lane
            !yourTeamChamps.hasOwnProperty(dropdown.value) &&
            !Object.values(yourTeamChamps).includes(dropdownPosition.value)) { // not already added
            updateChampionImage(dropdown.value, champContainer, yourTeamCounter, dropdownPosition.value);
            yourTeamCounter.value++;
            yourTeamChamps[dropdown.value] = dropdownPosition.value;
        } else if (teamType === 'enemyTeam' &&
            enemyTeamCounter.value < maxChampions && // no more than 5 champs
            dropdown.value != '' && // no blank champ
            dropdownPosition.value != '' && // no blank lane
            !enemyTeamChamps.hasOwnProperty(dropdown.value) &&
            !Object.values(enemyTeamChamps).includes(dropdownPosition.value)) { // not already added
            updateChampionImage(dropdown.value, champContainer, enemyTeamCounter, dropdownPosition.value);
            enemyTeamCounter.value++;
            enemyTeamChamps[dropdown.value] = dropdownPosition.value;
        }

        updateCalculateWinRateButton();
    });


};
function updateCalculateWinRateButton() {
    document.getElementById('yourChampion').style.display = 'none';
    if (yourTeamContainer.children.length === 5 && enemyTeamContainer.children.length === 5) {
        // If there are 5 champions on both sides, show the button
        calculateWinRateButton.style.display = 'grid';
        calculateWinRateButton.style.margin = '5px';
        yourChampDropdown.style.display = 'grid';
        yourChampContainer.style.display = 'grid';
        Object.keys(yourTeamChamps).forEach(championName => {
            const option = document.createElement('option');
            option.value = championName;
            option.textContent = championName;
            yourChampDropdown.appendChild(option);
        });
    } else {
        // Otherwise, hide the button
        yourChampDropdown.style.display = 'none';
        calculateWinRateButton.style.display = 'none';
        yourChampContainer.style.display = 'none';
    }
}

calculateWinRateButton.addEventListener('click', function () {
    if (document.getElementById('currentResultsCard')) {
        document.getElementById('currentResultsCard').remove();
    }
    if (document.getElementById('suggestionsCard')) {
        document.getElementById('suggestionsCard').remove();
    }
    ownChampion = yourChampDropdown.value;
    ownLane = yourTeamChamps[ownChampion];
    let data = {};
    // key = champ name // value = lane
    for (const [key, value] of Object.entries(yourTeamChamps)) {
        let newKey = value.toUpperCase() + "1";
        let newValue = champMapping[key];
        data[newKey] = newValue;
    }
    for (const [key, value] of Object.entries(enemyTeamChamps)) {
        let newKey = value.toUpperCase() + "2";
        let newValue = champMapping[key];
        data[newKey] = newValue;
    }

    // const data = {
    //     "JUNGLE1": "Jax",
    //     "JUNGLE2": "Skarner",
    //     "TOP1": "Fiora",
    //     "TOP2": "Galio",
    //     "MID1": "Viktor",
    //     "SUPPORT2": "VelKoz",
    //     "MID2": "Ahri",
    //     "SUPPORT1": "Nami",
    //     "CARRY1": "Draven",
    //     "CARRY2": "Jinx"
    // };
    //
    // response_data = 
    // [
    //     [
    //         [
    //             "darius",
    //             0.49846279257933235
    //         ],
    //         [
    //             "fiora",
    //             0.49846279257933235
    //         ],
    //         [
    //             "gangplank",
    //             0.49846279257933235
    //         ],
    //         [
    //             "jax",
    //             0.49846279257933235
    //         ],
    //         [
    //             "aatrox",
    //             0.49704880750981806
    //         ]
    //     ],
    //     {
    //         "Current": 0.49704880750981806
    //     }
    // ]

    fetch(`http://localhost:8080/predict?role=${ownLane.toUpperCase()}1`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(data => {
        currentReponse = data[1]["Current"];
        suggestionResponse = {};
        suggestionArray = data[0];
        suggestionArray.forEach(entry => {
            let key = entry[0];
            let val = entry[1];
            suggestionResponse[key] = val;
        });
        // -------------- Current Result Card
        const currentResults = document.createElement('card');
        currentResults.setAttribute('id', 'currentResultsCard');
        if(data.current >= 0.5){
            currentResults.setAttribute('style', 'background: lightgreen;width:300px; text-align: center; margin: 10px;');
        } else {
            currentResults.setAttribute('style', 'background: lightpink; width:300px; text-align: center; margin: 10px;');
        }
        currentResults.classList.add('card', 'align-items-center', 'current-result-element');
        const currentResultsContainer = document.createElement('container');
        currentResultsContainer.setAttribute('id', 'currentResults');
        currentResults.appendChild(currentResultsContainer);
        // Create the name element
        const crTitle = document.createElement('h6');
        crTitle.textContent = `Winning Chances with: ${ownChampion}`;
        crTitle.classList.add('ms-2', 'cr-title');
        currentResultsContainer.appendChild(crTitle);

            // Create the name element
            const crValue = document.createElement('p');
            crValue.textContent = `${(currentReponse * 100).toPrecision(2)}%`;
            crValue.classList.add('ms-2', 'cr-value');
            currentResultsContainer.appendChild(crValue);

            // ------------- Suggestion Card
            const suggestions = document.createElement('card');
            suggestions.setAttribute('id', 'suggestionsCard');
            if (data.current >= 0.5) {
                suggestions.setAttribute('style', 'background: lightgreen;width:300px; text-align: center; margin: 10px;');
            } else {
                suggestions.setAttribute('style', 'background: lightpink; width:300px; text-align: center; margin: 10px;');
            }
            suggestions.classList.add('card', 'align-items-center', 'suggestions-element');
            const suggestionsContainer = document.createElement('container');
            suggestionsContainer.setAttribute('id', 'currentResults');
            suggestions.appendChild(suggestionsContainer);

            // Create the name element
            const suggestionsTitle = document.createElement('h6');
            suggestionsTitle.textContent = 'Alternative Champion Suggestions Ranked';
            suggestionsTitle.classList.add('ms-2', 'cr-title');
            suggestionsContainer.appendChild(suggestionsTitle);

            // Create the name element
            const suggestionsValue = document.createElement('p');
            let suggestionsString = '';
            let counter = 1 ;
            for (const [key, value] of Object.entries(suggestionResponse)) {
                if (key != 'current') {
                    suggestionsString += `${counter}). ${key}: ${(value * 100).toPrecision(2)}%<br>`;
                }
                counter++;
            }
            suggestionsValue.innerHTML = suggestionsString;
            suggestionsValue.classList.add('ms-2', 'cr-value');
            suggestionsContainer.appendChild(suggestionsValue);


            resultsConatiner.appendChild(currentResults);
            resultsConatiner.appendChild(suggestions);
        })
        .catch((error) => {
            console.error('Error:', error);
        });
});

resetButton.addEventListener('click', function () {
    counter['value'] = 0;

    // Counters for each side
    yourTeamCounter = { value: 0 };
    yourTeamChamps = {};
    enemyTeamCounter = { value: 0 };
    enemyTeamChamps = {};
    ownChampion = '';
    const cards = document.querySelectorAll('.card');
    for (let i = 0; i < cards.length; i++) {
        cards[i].remove();
    }
    yourChampDropdown.innerHTML = '';
    updateCalculateWinRateButton()
});

populateDropdown('your-team-dropdown', 'yourTeam', 'yourTeam', 'your-team-position-dropdown', 'your-button');
populateDropdown('enemy-team-dropdown', 'enemyTeam', 'enemyTeam', 'enemy-team-position-dropdown', 'enemy-button');