'use strict';

const fs = require('fs');

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', function(inputStdin) {
    inputString += inputStdin;
});

process.stdin.on('end', function() {
    inputString = inputString.split('\n');

    main();
});

function readLine() {
    return inputString[currentLine++];
}



/*
 * Complete the 'getTotalGoals' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. STRING team
 *  2. INTEGER year
 */
const request = require('request')

async function sumPage(url,team){
    let rs = 0
    return new Promise(resolve=>{
        request(url,function(error,res,body){
            body = JSON.parse(body)
            body.data.forEach(obj=>{
                if (team === 1){
                    rs += obj.team1goals*1
                } else{
                    rs += obj.team2goals*1
                }
            })
            resolve(rs)            
        })
    })
}

async function GetData(url){
    let rs = 0
    return new Promise(resolve => {
        request(url, function(error, res, body){
            body = JSON.parse(body)
            resolve(body)
        })
    })
}

async function getTotalGoals(team, year) {
    let ans = 0
    const BaseUrl = `https://jsonmock.hackerrank.com/api/football_matches?year=${year}&`
    let team1Data = await GetData(BaseUrl+`team1=${team}`)
    for (let page=1; page<=team1Data.total_pages; page++){
        ans += await sumPage(BaseUrl+`team1=${team}&page=${page}`,1)
    }
    let team2Data = await GetData(BaseUrl+`team2=${team}`)
    for (let page=1; page<=team2Data.total_pages; page++){
        ans += await sumPage(BaseUrl+`team2=${team}&page=${page}`,2)
    }
    
    return ans
}

async function main() {