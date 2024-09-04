export default function Review({params}:{params:{reviewID:string}}){
    return <h1> Product {params.productID} Review {params.reviewID}</h1>;  
} 