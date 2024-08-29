function onDelete() {
  document.querySelector('#delete-form').addEventListener('submit', function (event) {
    if (!confirm('Are you sure you want to delete this item "{{ object }}"?')) {
      event.preventDefault() // Prevent form submission if the user cancels
    }
  })

  
 }