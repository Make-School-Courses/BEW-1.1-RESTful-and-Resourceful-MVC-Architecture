User.find()
.then(users) {

}.catch(e) {

};

Article.findByID(id)
.then(article) {

}.catch(e) {

};

User.find({ ssn: 123403921 })
.then(user) {

}.catch(e) {

};

Dogs.find({ goesToHeaven: true })
.sort({ name: 1 })
.then(dogs) {

}.catch(e) {

};
