document.addEventListener('DOMContentLoaded', function(){
    

});

function joinCourse(course_id){

    fetch('join/'+course_id, {
        method: 'PUT',   
    })
    .then(response => response.json())
    .then(data => {
        console.log(data)
        let j_button = document.querySelector(`#join_Course_${data.course_s_name}`);
        j_button.setAttribute('onclick', `window.location='course_page/${course_id}'`);

        j_button.innerHTML = "Start";
    })  
}

function dropCourse(course_id){
    if(confirm("Are you sure you want to drop this Class?")){
        fetch('drop_course/'+course_id, {
            method: 'POST',
        })
        .then(response => response.json())
        .then(data => {
            console.log(data)
            let delete_item;
            delete_item = document.querySelector('#course_entry_dashboard' + course_id);
            delete_item.remove();
        })
    }
}