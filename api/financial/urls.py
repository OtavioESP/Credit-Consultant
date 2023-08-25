from django.urls import path, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from financial.views import ProposalStatusView, ProposalFieldsView, FinancialProposalView

router = routers.SimpleRouter(trailing_slash=False)
router.register('proposal-status', ProposalStatusView,
                basename='proposal-status')
router.register('proposal-fields', ProposalFieldsView,
                basename='proposal-fields')
router.register('financial-proposal', FinancialProposalView,
                basename='financial-proposal')

urlpatterns = [
    path('', include(router.urls)),
] + router.urls

urlpatterns = format_suffix_patterns(urlpatterns)
