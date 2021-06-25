from import_export import resources
from perpustakaan.models import Buku

# declaration name column
from import_export.fields import Field


class BukuResource(resources.ModelResource):

    # declaration field
    kelompok_id__nama = Field(attribute = 'kelompok_id', column_name = 'kelompok')

    class Meta:
        model = Buku
        # get selected column to export
        fields = ['judul', 'tanggal', 'kelompok_id__nama', 'penerbit', 'jumlah']
        export_order = ['judul', 'kelompok_id__nama', 'tanggal', 'penerbit', 'jumlah']
