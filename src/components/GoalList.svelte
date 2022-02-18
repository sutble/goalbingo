<script>
    import { createEventDispatcher } from 'svelte';
    import slist from '../utils/sortable.js'

    const dispatch = createEventDispatcher();
    let target;

    
    let goalMap = {}
    for (let i = 1; i < 26; i++){
        goalMap[i] = ""
    }

    window.addEventListener("DOMContentLoaded", () => {
        target = document.getElementById("sortlist")
        slist(target,updateText);
    })

    function updateText(e){
        if (e && e.path && e.path.length > 0){
            let input = e.path[0]
            input.placeholder = "";
        }
        let items = target.children
        for (let i = 0; i < items.length; i++){
            let item = items[i]
            let text = item.children[0].value
            goalMap[26-(i+1)] = text
        }
        
        dispatch('updatedGoals', {
			goalMap
		});
    }
</script>

<style>
.slist {
  
  padding: 10;
  margin: 0;
  width: 500px;
}
.slist li {
  margin: 10px;
  padding: 15px;
  border: 1px solid #dfdfdf;
  background: #f5f5f5;
}

.slist li input {
  margin: 0px;
  padding: 15px;
  border: 1px solid #dfdfdf;
  background: #ffffff;
  width: 100%
}

.slist li.hint {
  border: 1px solid #ffc49a;
  background: #feffb4;
}
.slist li.active {
  border: 1px solid #ffa5a5;
  background: #ffe7e7;
}
</style>

<div class="goal-list">
    <ol class="slist" id="sortlist">
        <li> <input placeholder = "Hardest goal" id="25" on:input={updateText}/> </li>
        <li> <input id="24" on:input={updateText}/> </li>
        <li> <input id="23" on:input={updateText}/> </li>
        <li> <input id="22" on:input={updateText}/> </li>
        <li> <input id="21" on:input={updateText}/> </li>
        <li> <input id="20" on:input={updateText}/> </li>
        <li> <input id="19" on:input={updateText}/> </li>
        <li> <input id="18" on:input={updateText}/> </li>
        <li> <input id="17" on:input={updateText}/> </li>
        <li> <input id="16" on:input={updateText}/> </li>
        <li> <input id="15" on:input={updateText}/> </li>
        <li> <input id="14" on:input={updateText}/> </li>
        <li> <input id="13" on:input={updateText}/> </li>
        <li> <input id="12" on:input={updateText}/> </li>
        <li> <input id="11" on:input={updateText}/> </li>
        <li> <input id="10" on:input={updateText}/> </li>
        <li> <input id="9" on:input={updateText}/> </li>
        <li> <input id="8" on:input={updateText}/> </li>
        <li> <input id="7" on:input={updateText}/> </li>
        <li> <input id="6" on:input={updateText}/> </li>
        <li> <input id="5" on:input={updateText}/> </li>
        <li> <input id="4" on:input={updateText}/> </li>
        <li> <input id="3" on:input={updateText}/> </li>
        <li> <input id="2" on:input={updateText}/> </li>
        <li> <input placeholder = "Easiest goal" id="1" on:input={updateText}/> </li>
      </ol>
</div>