// label_center = document.getElementsByTagName('label')[0]
// label_center.innerHTML = '<h2 style="text-align:center;">What to do</h2>'
// label_center.className = "text-center"
actions = document.querySelectorAll('.makeAction');
action = null
for(i =0; i < actions.length; i++){
    actions[i].addEventListener('click', function(){
        if(this.dataset.add == 'add'){
            action = this.dataset.add
        }
        else if(this.dataset.remove == 'remove'){
      action = 'remove'
      
        }
        todo_id = this.dataset.id

        
        if(this.dataset.remove == 'remove'){
   url = '/delete_todo/'
     fetch(url,{
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
            'Accept': 'application/json'
        }, 
         body: JSON.stringify({'action': action, 'todo_id': todo_id})
     })
     .then(res=>{ 
        this.parentElement.parentElement.className = "hidden"
        return res.json();
        
     }
        )
     .then(data=>console.log(data)) 
    }
    }
    )
}
