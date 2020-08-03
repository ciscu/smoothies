<template>
  <div class="index container">
    <div v-for="smoothie in smoothies" :key="smoothie.id" class="card">
     <div class="card-content">
       <i class="material-icons delete" @click="deleteSmoothie(smoothie.id)">delete</i>
       <h2 class="indigo-text">{{smoothie.title}}</h2>
       <ul class="ingredients">
         <li v-for="(ingredient, index) in smoothie.ingredients" :key="index">
           <span class="chip">{{ingredient}}</span>
         </li>
       </ul>
     </div> 
     <span class="btn-floating btn-large halfway-fab pink">
       <router-link :to="{ name: 'EditSmoothie', params: {smoothie_name: smoothie.title} }"><i class="material-icons edit">edit</i></router-link>
     </span>
    </div>
  </div>
</template>
    
<script>
import db from '@/firebase/init'
export default {
  name: 'Index',
  data () {
    return {
      smoothies: []
    }
  },
  methods: {
    deleteSmoothie(id) {
      fetch(`http://localhost:5000/smoothies/delete/${id}`, {
        method: 'DELETE'
      })
      .then(response => response.json())
      .then(data => {
        this.smoothies = this.smoothies.filter(smoothie => smoothie.id !== id)
      })

    }
  },
  created() {
    fetch("http://localhost:5000/api/v1/smoothies/")
      .then(response => response.json())
      .then(data => data["smoothies"].forEach(smoothie => {
        fetch(`http://localhost:5000/api/v1/smoothies/${smoothie["name"]}`)
        .then(response => response.json())
        .then(data => {
          let newSmoothie = {
            id: data["id"],
            title: data["name"],
            ingredients: data["ingredients"]
          }
          this.smoothies.push(newSmoothie)
        })
        }
        ))
  }
}
</script>

<style>
.index{
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  grid-gap: 30px;
  margin-top: 60px;

}
.index h2 {
  font-size: 1.8em;
  text-align: center;
  margin-top: 0;
}
.index .ingredients {
  margin: 30px auto;
}
.index .ingredients li{
  display: inline-block;
}
.index .delete{
  position: absolute;
  top: 4px;
  right: 4px;
  cursor: pointer;
  color: #aaa;
  font-size: 1.4em
}
</style>
