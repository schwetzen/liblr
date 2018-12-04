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

  // TODO: Move to separate file
  // Automatically send request when filter key changes:
  let form = document.getElementById('filterForm')
  let filter = form.querySelector('#filter')

  let selected = form.querySelector('#filter_key')
  if (selected) {
    filter.value = selected.value
    form.removeChild(selected)
  }

  filter.onchange = () => {
    let input = document.createElement('input')

    if (filter.value) {
      input.setAttribute('type', 'hidden')
      input.setAttribute('name', 'filter')
      input.setAttribute('value', filter.value)
      form.appendChild(input)
    }

    form.submit()
  }
})
