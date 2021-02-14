async function api(i){
    return new Promise(resolve=>{
        setTimeout(() => {
           console.log(`${i}초 이후 출력`) 
           console.log(new Date())
        }, i*1000);
    })
}

const all = async ()=>{
    const arr = [3,1,5]
    const arrPromises = arr.map(api)
    await Promise.all(arrPromises)
}

// output
// all()
// Promise {<pending>}
// VM22:4 1초 이후 출력
// VM22:5 Sun Feb 14 2021 15:25:06 GMT+0900 (대한민국 표준시)
// VM22:4 3초 이후 출력
// VM22:5 Sun Feb 14 2021 15:25:08 GMT+0900 (대한민국 표준시)
// VM22:4 5초 이후 출력
