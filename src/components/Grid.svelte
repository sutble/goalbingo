<script>
    export let goalMap
    for (let i = 1; i < 26; i++){
        goalMap[i] = "FREE SPACE"
    }
    //let ids = ["1a","2a","3a","4a","5a","1b","2b","3b","4b","5b","1c","2c","3c","4c","5c","1d","2d","3d","4d","5d","1e","2e","3e","4e","5e"]
</script>

<style>
    .grid-5-by-5 {

        /* Activate grid layout */
        display: grid;

        /* Create 5 columns, each 1 "fractional unit" wide */
        grid-template-columns: repeat(5, 110px);

        /* Create 5 rows, each 1 "fractional unit" high */
        grid-template-rows: repeat(5);

        /* Add a 10px gap between columns and rows */
        grid-gap: 1px;
    }

    .item {
    background-color: rgba(229, 229, 229, 0.5);
    border: 1px solid rgba(128, 128, 128, 0.5);
    padding: 0.25em;
    height: 100px;
    width: 100px;
    align-items: center;
    justify-content: center;
    display: flex
    }
</style>
<div class="grid-5-by-5">
    <div class="item" id="1a">{goalMap[15]}</div>
    <div class="item" id="2a">{goalMap[5]}</div>
    <div class="item" id="3a">{goalMap[6]}</div>
    <div class="item" id="4a">{goalMap[22]}</div>
    <div class="item" id="5a">{goalMap[17]}</div>
    <div class="item" id="1b">{goalMap[21]}</div>
    <div class="item" id="2b">{goalMap[10]}</div>
    <div class="item" id="3b">{goalMap[3]}</div>
    <div class="item" id="4b">{goalMap[8]}</div>
    <div class="item" id="5b">{goalMap[23]}</div>
    <div class="item" id="1c">{goalMap[9]}</div>
    <div class="item" id="2c">{goalMap[16]}</div>
    <div class="item" id="3c">{goalMap[25]}</div>
    <div class="item" id="4c">{goalMap[4]}</div>
    <div class="item" id="5c">{goalMap[11]}</div>
    <div class="item" id="1d">{goalMap[19]}</div>
    <div class="item" id="2d">{goalMap[14]}</div>
    <div class="item" id="3d">{goalMap[7]}</div>
    <div class="item" id="4d">{goalMap[13]}</div>
    <div class="item" id="5d">{goalMap[12]}</div>
    <div class="item" id="1e">{goalMap[1]}</div>
    <div class="item" id="2e">{goalMap[20]}</div>
    <div class="item" id="3e">{goalMap[24]}</div>
    <div class="item" id="4e">{goalMap[18]}</div>
    <div class="item" id="5e">{goalMap[2]}</div>
</div>