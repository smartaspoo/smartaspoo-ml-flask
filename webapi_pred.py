import flask
from flask import Flask, request, jsonify, make_response

# Initialize Flask app
app = flask.Flask(__name__)

data_barang =[
    {
        'nama':'Jenang Mubarok',
        'id':'1',
        'harga':'25000'
    },
    {
        'nama':'Carica',
        'id':'2',
        'harga':'10000'
    },
    {
        'nama':'Keripik Singkong',
        'id':'3',
        'harga':'12000'
    }
]

# Get all barang
@app.route('/')
def welcome():
    return  """ <h1>Welcome to Python Web Service</h1>
                <p>Click <a href = "/databarang/getDataBarang">here</a> to view all Data Barang</p>
            """

# Routing Get Data
@app.route('/databarang/getDataBarang', methods = ['GET'])
def getDataBarang():
    return jsonify(data_barang)

# Routing Get Data Barang (search id)
@app.route('/databarang/getDataBarang/<id>', methods = ['GET'])
def getDataBarangs(id):
    data_brg = [brg for brg in data_barang if(brg['id'] == id)]
    if(len(data_brg) > 0):
        return jsonify(data_brg)
    else:
        return make_response(jsonify({"message": "Data Barang tidak ditemukan"}), 404)

# Routing Updata Data Barang
@app.route('/databarang/updateDataBarang/<id>', methods = ['PUT'])
def updateDataBarang(id):
    data_brg = [brg for brg in data_barang if(brg['id'] == id)] #byid
    if(len(data_brg) > 0):
        if 'nama' in request.json and 'harga' in request.json:
            data_brg[0]['nama'] = request.json['nama']
            data_brg[0]['harga'] = request.json['harga']
        return make_response(jsonify({"message": "Data Barang berhasil diperbarui"}), 200)
    else:
        return make_response(jsonify({"message": "Data Barang tidak ditemukan"}), 400)

# Routing Add Data Barang
@app.route('/databarang/addDataBarang', methods = ['POST'])
def addDataBarang():
    brg = {
        'nama':request.json['nama'],
        'id':request.json['id'],
        'harga':request.json['harga']
    }
    if (brg['nama'] and brg['id'] and brg['harga']):
        data_barang.append(brg)
        return make_response(jsonify({"message": "Data Barang berhasil ditambahkan"}), 201)
    else:
        return make_response(jsonify({"message": "Data Barang tidak lengkap"}), 400)

# Routing Delete Data Barang
@app.route('/databarang/deleteDataBarang/<brgid>', methods = ['DELETE'])
def deleteDataBarang(brgid):
    data_brg = [brg for brg in data_barang if (brg['id']==brgid)]
    if(len(data_brg) > 0):
        data_barang.remove(data_brg[0])
        return make_response(jsonify({"message": "Data Barang berhasil dihapus"}), 200)
    else:
        return make_response(jsonify({"message": "Data Barang tidak ditemukan"}), 404)

if(__name__ == "__main__"):
    app.run(debug=True)
