$(document).ready(function() {
  let forms = document.querySelectorAll('.form')

  forms.forEach(form => {
    let method = form.getAttribute('method').toLowerCase()

    switch (method) {
      case 'put':
      case 'patch':
      case 'delete':
        let input = document.createElement('input')
        input.setAttribute('type', 'hidden')
        input.setAttribute('name', 'http_method')
        input.setAttribute('value', method)
        form.appendChild(input)
        form.setAttribute('method', 'post')
      default:
        break
    }
  })
})
