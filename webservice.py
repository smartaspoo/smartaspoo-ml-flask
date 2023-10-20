import flask
from flask import Flask, request, jsonify, redirect
import requests

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

# Routing Welcome Page
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
        return jsonify({"message": "Data Barang tidak ditemukan"})

# Routing Updata Data Barang
@app.route('/databarang/updateDataBarang/<id>', methods = ['PUT'])
def updateDataBarang(id):
    data_brg = [brg for brg in data_barang if(brg['id'] == id)] #byid
    if(len(data_brg) > 0):
        if 'nama' in request.json and 'harga' in request.json:
            data_brg[0]['nama'] = request.json['nama']
            data_brg[0]['harga'] = request.json['harga']
        return jsonify({"message": "Data Barang berhasil diperbarui"})
    else:
        return jsonify({"message": "Data Barang tidak ditemukan"})

# Routing Add Data Barang
@app.route('/databarang/addDataBarang', methods = ['POST'])
def addDataBarang():
    brg = {
        'nama':request.json['nama'],
        'id':request.json['id'],
        'harga':request.json['harga']
    }
    data_barang.append(brg)
    return jsonify({"message": "Data Barang berhasil ditambahkan"})

# Routing Delete Data Barang
@app.route('/databarang/deleteDataBarang/<brgid>', methods = ['DELETE'])
def deleteDataBarang(brgid):
    data_brg = [brg for brg in data_barang if (brg['id']==brgid)]
    if(len(data_brg) > 0):
        data_barang.remove(data_brg[0])
        return jsonify({"message": "Data Barang berhasil dihapus"})
    else:
        return jsonify({"message": "Data Barang tidak ditemukan"})

if(__name__ == "__main__"):
    app.run(debug=True)
