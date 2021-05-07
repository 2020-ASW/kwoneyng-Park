function find(x,rooms){
    if (rooms.has(x)){
        rooms.set(x,find(rooms.get(x),rooms))
        return rooms.get(x)
    }
    rooms.set(x,x+1)
    return x
}


function solution(k, room_number) {
    var answer = [];
    const rooms = new Map()
    room_number.forEach(room=>{
        let checkIn = find(room,rooms)
        answer.push(checkIn)
    })
    
    
    return answer;
}