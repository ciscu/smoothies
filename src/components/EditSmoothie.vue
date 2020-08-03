<template>
    <div v-if="smoothie" class="edit-smoothie container">
        <h2>Edit {{ smoothie.title }}</h2>
        <form @submit.prevent="EditSmoothie">
            <div class="field title">
                <label for="title">Smoothie Title:</label>
                <input type="text" name="title" v-model="smoothie.title">
            </div>
            <div v-for="(ingredient, index) of smoothie.ingredients" :key="index" class="field">
                <label for="ingredient">Ingredient:</label>
                <input type="text" name="ingredient" v-model="smoothie.ingredients[index]">
                <i class="material-icons delete" @click="deleteIngredient(ingredient)">delete</i>

            </div>
            <div v-if="smoothie.title" class="field add-ingredient">
                <label for="add-ingredient">Ad an ingredient:</label>
                <input type="text" name="add-ingredient" @keydown.tab.prevent="addIngredient" v-model="ingredient">
            </div>
            <div class="field center-align">
                <p v-if="feedback" class="red-text">{{ feedback }}</p>
                <button class="btn pink">Edit Smoothie</button>
            </div>
        </form>
    </div>
    
</template>

<script>
import db from '@/firebase/init'
import slugify from 'slugify'
export default {

    name: 'EditSmoothie',
    data(){
       return {
           slug: this.$route.params.smoothie_name,
           smoothie: null,
           ingredient: null,
           feedback: null

       }
   },
   methods: {
       EditSmoothie() {
            if(this.smoothie.title){
                this.feedback = null
                this.smoothie.slug = slugify(this.smoothie.title, {
                    replacement: '-',
                    remove: /[$*_+~.()'"!\-:@]/g,
                    lower: true
                })
                fetch(`http://localhost:5000/api/v1/smoothies/edit/${this.smoothie.id}`, {
                    method: "PUT",
                    headers: {
                        'Accept': 'application/json',
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        name: this.smoothie.title,
                        ingredients: this.smoothie.ingredients
                    })
                }).then(() => this.$router.push({name: 'Index'}))
            }else {
                this.feedback = "You must enter a smoothie title"
            }
       },
       addIngredient() {
            if(this.ingredient){
                this.smoothie.ingredients.push(this.ingredient)
                this.ingredient = null
                this.feedback = null
            }
            else{
                this.feedback = "You must enter a value in order to add an ingredient"
            }
        },
       deleteIngredient(id) {
           this.smoothie.ingredients = this.smoothie.ingredients.filter(ingredient => ingredient !== id)
       }
   },
   created() {
    fetch(`http://localhost:5000/api/v1/smoothies/${this.slug}`)
    .then(response => response.json())
    .then(data => {
        this.smoothie = data
        this.smoothie.title = data["name"]
        })
   }
}
</script>

<style>
    .edit-smoothie{
        margin-top: 60px;
        padding: 20px;
        max-width: 500px;
    }
    .edit-smoothie h2{
        font-size: 2em;
        margin: 20px auto;
    }
    .edit-smoothie .field{
        margin: 20px auto;
        position: relative;
    }
    .edit-smoothie .delete{
        cursor: pointer; 
        position: absolute;
        right: 0;
        bottom: 16px;
        color: #aaa;
        font-size: 1.4em;
    }
</style>