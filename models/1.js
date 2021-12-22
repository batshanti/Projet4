class Tournament{
    constructor(players, rounds, currentRound = 1) {
        this.players = players
        this.rounds = rounds
        this.currentRound = currentRound
    }
    
    
//        static
    getTournamentById(id){
        let rawData = table.get("select * tournaments where id = ?", {id})
        let players = rawData.players
        let playerListObjects = []
        for (let player in players) {
            let newPlayer = new Player(player.name)
            playerListObjects.push(newPlayer)
        }
        return new Tournament(playerListObjects, [], rawData.currentRound)
    }
    
    save(){
        let playerSerialized = []
        for (let player in this.players) {
            playerSerialized.push(player.serialized)
        }
        tournamentInfoSerialized = {
            players : playerSerialized,
            name: this.name
        }
        table.update("update tournaments where id = ?", {})
    }
    
    addResultToMatchInCurrentRound(matchId, score){
        this.rounds[this.currentRound].addResultToMatch(matchId, score)
        this.save()
    }
}


class Round {
    constructor(matchs) {
        this.matchs = matchs
    }
    
    addResultToMatch(matchId, score){
        this.matchs[matchId].score = score
    }
}

class Match {
    constructor(player1, player2, score = null) {
        this.player1 = player1
        this.player2 = player2
        this.score = score
    }
}

class Player {
    constructor(name = name) {
        this.name = name
    }
    
    serialized(){
        return {
            name: this.name
        }
    }
}


let player1 = new Player("player1")
let player2 = new Player("player2")
let player3 = new Player("player3")
let player4 = new Player("player4")

let players = [player1, player2, player3, player4]
let myTournament = new Tournament(players, [], 1)
myTournament.addResultToMatchInCurrentRound(1, [1, 0])


let myTournamentId1 = Tournament.getTournamentById(1)